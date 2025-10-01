from PIL import Image, ImageTk
import tkinter as tk
from pathlib import Path
from app.controllers.zoomImage import zoomImage

def showImage(imageContainer, imageData):
    """
    imageData: dict with keys 'path', 'name', 'description'
    """
    if not imageData:
        return

    # Clear previous content
    for widget in imageContainer.winfo_children():
        widget.destroy()

    imagePath = imageData["path"]
    imageName = imageData.get("name", Path(imagePath).stem)
    imageDesc = imageData.get("description", "")

    # Load and resize image
    img = Image.open(imagePath)
    img.thumbnail((500, 500))
    tk_img = ImageTk.PhotoImage(img)

    # Keep a reference
    imageContainer.tk_image = tk_img

    # Frame for image
    frame = tk.Frame(imageContainer, bd=2, relief="groove", bg="#fff")
    frame.pack(pady=20, padx=20)

    lbl_img = tk.Label(frame, image=tk_img, bg="#fff")
    lbl_img.pack(padx=10, pady=10)

    # Name label
    lbl_name = tk.Label(imageContainer, text=imageName, font=("Arial", 12, "bold"), bg="#f0f0f0")
    lbl_name.pack(pady=(5, 2))

    # Description label
    lbl_desc = tk.Label(imageContainer, text=imageDesc, font=("Arial", 10), bg="#f0f0f0",
                        wraplength=500, justify="left")
    lbl_desc.pack(pady=(0, 15))

    lbl_img.bind("<Button-1>", lambda e: zoomImage(imagePath))

