from PIL import Image, ImageTk
import tkinter as tk
from pathlib import Path
from app.controllers.zoomImage import zoomImage

def showImage(parentContainer, imageData):
    """
    imageData: dict with keys 'path', 'name', 'description'
    """
    if not imageData:
        return

    # Clear previous content
    for widget in parentContainer.winfo_children():
        widget.destroy()

    # Create canvas + scrollbar
    canvas = tk.Canvas(parentContainer, bg="#f0f0f0")
    scrollbar = tk.Scrollbar(parentContainer, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Load image
    imagePath = imageData["path"]
    imageName = imageData.get("name", Path(imagePath).stem)
    imageDesc = imageData.get("description", "")

    img = Image.open(imagePath)
    img.thumbnail((700, 700))
    tk_img = ImageTk.PhotoImage(img)
    scrollable_frame.tk_image = tk_img  # keep reference

    # Frame for image
    frame = tk.Frame(scrollable_frame, bd=2, relief="groove", bg="#fff")
    frame.pack(pady=20, padx=20)

    lbl_img = tk.Label(frame, image=tk_img, bg="#fff")
    lbl_img.pack(padx=10, pady=10)
    lbl_img.bind("<Button-1>", lambda e: zoomImage(imagePath))

    # Name label
    lbl_name = tk.Label(scrollable_frame, text=imageName, font=("Arial", 12, "bold"), bg="#f0f0f0")
    lbl_name.pack(pady=(5, 2))

    # Description label
    lbl_desc = tk.Label(scrollable_frame, text=imageDesc, font=("Arial", 10), bg="#f0f0f0",
                        wraplength=500, justify="left")
    lbl_desc.pack(pady=(0, 15))
