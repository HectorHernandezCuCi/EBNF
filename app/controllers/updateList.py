import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path

def updateList(listFrame, imagesList, onClick=None):
    for widget in listFrame.winfo_children():
        widget.destroy()

    listFrame.imagesRefs = []

    for imgData in imagesList:
        imgPath = imgData["path"]
        img = Image.open(imgPath)
        img.thumbnail((200, 200))
        tkImg = ImageTk.PhotoImage(img)
        listFrame.imagesRefs.append(tkImg)

        imgContainer = tk.Frame(listFrame, bg="white", relief="raised", bd=1)
        imgContainer.pack(side='top', anchor='w', padx=5, pady=5, fill="x")

        labelImage = tk.Label(imgContainer, image=tkImg, bg="white", cursor="hand2")
        labelImage.pack(side='left', padx=10, pady=5)

        labelName = tk.Label(imgContainer, text=imgData.get("name", Path(imgPath).stem), 
                             font=("Arial", 11), bg="white", cursor="hand2")
        labelName.pack(side='left', padx=10)

        # Hover effect
        def on_enter(e, w=imgContainer):
            w.config(bg="#e0f7fa")
        def on_leave(e, w=imgContainer):
            w.config(bg="white")

        imgContainer.bind("<Enter>", on_enter)
        imgContainer.bind("<Leave>", on_leave)

        if onClick:
            labelImage.bind('<Button-1>', lambda e, d=imgData: onClick(d))
            labelName.bind('<Button-1>', lambda e, d=imgData: onClick(d))
