import tkinter as tk
from app.controllers.showImage import showImage
from pathlib import Path

class ShowImageFrame(tk.Frame):
    def __init__(self, master, controller=None, **kwargs):
        super().__init__(master, **kwargs)

        self.imageContainer = tk.Frame(self)
        self.imageContainer.pack(fill='both', expand=True)

    def displayImage(self, imageData):
        """
        imageData: dict with keys 'path', 'name', 'description'
        """
        if isinstance(imageData, str):
            # If a string path is passed, convert to dict
            imageData = {
                "path": imageData,
                "name": Path(imageData).stem,
                "description": ""
            }
        showImage(self.imageContainer, imageData)
