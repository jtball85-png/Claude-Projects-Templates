"""
Page Capture Tool

A small GUI tool that captures a screenshot of a fixed screen region (a
"digital page" you're viewing, e.g. a PDF/e-book viewer) each time you press
a hotkey, reads the page number printed at the bottom of that region via OCR,
and saves the image as "<page_number>.png" in a folder you choose.

Double-click "Capture Pages.bat" in this same folder to launch it - no
command line needed. Everything (choosing the save folder, selecting the
screen region, capturing pages) is done through the window that opens.

Requirements (already installed for this project):
  - Tesseract OCR engine  (winget install UB-Mannheim.TesseractOCR)
  - pip packages: pytesseract, keyboard, mss, pillow
"""

import re
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

import keyboard
import mss
import pytesseract
from PIL import Image

TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
if Path(TESSERACT_PATH).exists():
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

HOTKEY = "f9"
STOP_KEY = "esc"
STRIP_FRACTION = 0.08


def grab(region: tuple[int, int, int, int]) -> Image.Image:
    left, top, width, height = region
    with mss.mss() as sct:
        monitor = {"left": left, "top": top, "width": width, "height": height}
        shot = sct.grab(monitor)
        return Image.frombytes("RGB", shot.size, shot.bgra, "raw", "BGRX")


def read_page_number(img: Image.Image, strip_fraction: float = STRIP_FRACTION) -> str | None:
    """OCR the bottom strip of the image and pull out the page number."""
    width, height = img.size
    strip_height = max(int(height * strip_fraction), 20)
    bottom_strip = img.crop((0, height - strip_height, width, height))
    bottom_strip = bottom_strip.resize(
        (bottom_strip.width * 3, bottom_strip.height * 3), Image.LANCZOS
    )
    config = "--psm 6 -c tessedit_char_whitelist=0123456789"
    text = pytesseract.image_to_string(bottom_strip, config=config)
    matches = re.findall(r"\d+", text)
    if not matches:
        return None
    return max(matches, key=len)


def unique_path(folder: Path, name: str, suffix: str) -> Path:
    candidate = folder / f"{name}{suffix}"
    n = 2
    while candidate.exists():
        candidate = folder / f"{name}_dup{n}{suffix}"
        n += 1
    return candidate


class CaptureApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Page Capture Tool")
        self.root.geometry("480x180")
        self.root.resizable(False, False)

        self.region = None
        self.out_dir = None
        self.unread_count = 0
        self.hotkeys_registered = False
        self.cap_win = None
        self.log_box = None

        self._build_setup_screen()
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    # ---------- Setup screen ----------

    def _build_setup_screen(self):
        pad = {"padx": 12, "pady": 8}

        tk.Label(self.root, text="Save pages to this folder:", font=("Segoe UI", 10)).pack(
            anchor="w", **pad
        )

        row = tk.Frame(self.root)
        row.pack(fill="x", padx=12)
        self.folder_var = tk.StringVar()
        entry = tk.Entry(row, textvariable=self.folder_var, font=("Segoe UI", 10))
        entry.pack(side="left", fill="x", expand=True, ipady=4)
        tk.Button(row, text="Browse...", command=self._browse).pack(side="left", padx=(8, 0))

        tk.Label(
            self.root,
            text="Next: you'll drag a box around the page area on screen (once),\n"
                 f"then press [{HOTKEY.upper()}] to capture each page.",
            fg="gray30",
            justify="left",
        ).pack(anchor="w", **pad)

        tk.Button(
            self.root, text="Start", font=("Segoe UI", 10, "bold"),
            command=self._start,
        ).pack(pady=10)

    def _browse(self):
        path = filedialog.askdirectory()
        if path:
            self.folder_var.set(path)

    def _start(self):
        folder = self.folder_var.get().strip()
        if not folder:
            messagebox.showerror("Page Capture Tool", "Please choose or type a folder to save pages into.")
            return
        try:
            Path(folder).mkdir(parents=True, exist_ok=True)
        except OSError as e:
            messagebox.showerror("Page Capture Tool", f"Couldn't use that folder:\n{e}")
            return
        self.out_dir = Path(folder)
        self.root.withdraw()
        self._select_region()

    # ---------- Region selection ----------

    def _select_region(self):
        overlay = tk.Toplevel(self.root)
        overlay.attributes("-fullscreen", True)
        overlay.attributes("-alpha", 0.25)
        overlay.attributes("-topmost", True)
        overlay.configure(bg="black")
        canvas = tk.Canvas(overlay, cursor="cross", bg="gray11", highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        canvas.create_text(
            overlay.winfo_screenwidth() // 2, 40,
            text="Click and drag a box around the page content, then release. (Esc to cancel)",
            fill="white", font=("Segoe UI", 16),
        )

        coords = {}
        state = {"rect": None}

        def on_press(event):
            coords["x0"], coords["y0"] = event.x, event.y

        def on_drag(event):
            if state["rect"] is not None:
                canvas.delete(state["rect"])
            state["rect"] = canvas.create_rectangle(
                coords["x0"], coords["y0"], event.x, event.y,
                outline="#00e0ff", width=2,
            )

        def on_release(event):
            coords["x1"], coords["y1"] = event.x, event.y
            left, right = sorted((coords["x0"], coords["x1"]))
            top, bottom = sorted((coords["y0"], coords["y1"]))
            self.region = (left, top, right - left, bottom - top)
            overlay.destroy()
            self._open_capture_window()

        def on_cancel(event=None):
            self.region = None
            overlay.destroy()
            self.root.deiconify()

        canvas.bind("<ButtonPress-1>", on_press)
        canvas.bind("<B1-Motion>", on_drag)
        canvas.bind("<ButtonRelease-1>", on_release)
        overlay.bind("<Escape>", on_cancel)

    # ---------- Capture window ----------

    def _open_capture_window(self):
        self.cap_win = tk.Toplevel(self.root)
        self.cap_win.title("Page Capture Tool - capturing")
        self.cap_win.geometry("420x320")
        self.cap_win.attributes("-topmost", True)
        self.cap_win.protocol("WM_DELETE_WINDOW", self._stop_capturing)

        tk.Label(
            self.cap_win,
            text=f"Saving to: {self.out_dir}",
            wraplength=400, justify="left", fg="gray20",
        ).pack(anchor="w", padx=10, pady=(10, 0))

        tk.Label(
            self.cap_win,
            text=f"In your viewer, go to a page and press [{HOTKEY.upper()}] to capture it.",
            wraplength=400, justify="left", font=("Segoe UI", 10, "bold"),
        ).pack(anchor="w", padx=10, pady=(6, 6))

        self.log_box = tk.Listbox(self.cap_win, font=("Consolas", 9))
        self.log_box.pack(fill="both", expand=True, padx=10, pady=(0, 6))

        tk.Button(self.cap_win, text="Stop", command=self._stop_capturing).pack(pady=(0, 10))

        keyboard.add_hotkey(HOTKEY, self._on_capture_pressed)
        keyboard.add_hotkey(STOP_KEY, self._on_stop_pressed)
        self.hotkeys_registered = True

        self._log(f"Region set. Ready - press {HOTKEY.upper()} to capture the current page.")

    def _log(self, text):
        if self.log_box is None:
            return
        self.log_box.insert("end", text)
        self.log_box.see("end")

    def _on_capture_pressed(self):
        # Runs on the keyboard library's own thread - hop back to the Tk thread.
        self.root.after(0, self._do_capture)

    def _on_stop_pressed(self):
        self.root.after(0, self._stop_capturing)

    def _do_capture(self):
        img = grab(self.region)
        page_number = read_page_number(img)
        if page_number:
            name = page_number
        else:
            self.unread_count += 1
            name = f"unrecognized_{self.unread_count}"
            self._log(f"  Could not read a page number - saving as {name}.png")
        path = unique_path(self.out_dir, name, ".png")
        img.save(path)
        self._log(f"Saved {path.name}")

    def _stop_capturing(self):
        if self.hotkeys_registered:
            keyboard.remove_hotkey(HOTKEY)
            keyboard.remove_hotkey(STOP_KEY)
            self.hotkeys_registered = False
        if self.cap_win is not None:
            self.cap_win.destroy()
            self.cap_win = None
        self.root.deiconify()

    def _on_close(self):
        if self.hotkeys_registered:
            keyboard.remove_hotkey(HOTKEY)
            keyboard.remove_hotkey(STOP_KEY)
        self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    CaptureApp().run()
