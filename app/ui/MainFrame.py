import tkinter as tk

class MainFrame(tk.Frame):
    def __init__(self, master, controller=None, **kwargs):
        super().__init__(master, **kwargs)

        # Title label
        tk.Label(
            self,
            text="Visualizador de diagramas",
            font=("Arial", 50, "bold"),
            bg=kwargs.get("bg", "#ffffff") 
        ).pack(pady=10)
