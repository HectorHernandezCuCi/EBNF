import tkinter as tk
from tkinter import ttk 
from app.controllers.addFile import addFile
from app.controllers.updateList import updateList
from app.controllers.getImageFromFolder import getImageFromFolder

class ListImageFrame(tk.Frame):
    def __init__(self, master, showFrame=None, controller=None, **kwargs):
        super().__init__(master, bg="#f0f0f0", padx=10, pady=10)

        # Title
        tk.Label(
            self, 
            text="Archivos de los diagramas", 
            font=("Arial", 22, "bold"), 
            bg="#f0f0f0"
        ).pack(pady=(0,15))

        # Add button
        tk.Button(
            self, 
            text="➕ Agregar Diagrama", 
            command=self.addNewFile, 
            bg="#4CAF50", 
            fg="white", 
            font=("Arial", 12, "bold"), 
            relief="flat", 
            padx=10, 
            pady=5,
            activebackground="#45a049"
        ).pack(pady=(0,15))

        # Scrollable list frame
        self.canvas = tk.Canvas(self, bg="#f0f0f0", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#f0f0f0")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.showFrame = showFrame
        self.images = getImageFromFolder('assets/img')
        self.updateList()

    def updateList(self):
        updateList(self.scrollable_frame, self.images, onClick=self.showFrame.displayImage if self.showFrame else None)
    
    def addNewFile(self):
        addFile(self.images, self.updateList)