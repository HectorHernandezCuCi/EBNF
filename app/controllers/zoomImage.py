import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path

def zoomImage(image_path):
    """Open a new window with the full-size image"""
    top = tk.Toplevel()
    top.title(Path(image_path).name)
    img = Image.open(image_path)
    tk_img = ImageTk.PhotoImage(img)
    top.tk_image = tk_img
    lbl = tk.Label(top, image=tk_img)
    lbl.pack()
    top.geometry(f"{img.width}x{img.height}")