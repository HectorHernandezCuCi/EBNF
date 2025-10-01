import tkinter as tk
from app.ui.MainFrame import MainFrame
from app.ui.ListImageFrame import ListImageFrame
from app.ui.ShowImageFrame import ShowImageFrame

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EBNF Viewer")
        self.geometry("1500x700")
        self.configure(bg="#f5f5f5")

        self.main_frame = MainFrame(self, bg="#ffffff", bd=2, relief="groove")
        self.show_frame = ShowImageFrame(self, bg="#ffffff", bd=2, relief="groove")
        self.list_frame = ListImageFrame(self, showFrame=self.show_frame, bg="#ffffff", bd=2, relief="groove")

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_columnconfigure(1, weight=2, uniform="group1")

        self.main_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=20, pady=15)
        self.list_frame.grid(row=1, column=0, sticky="nsew", padx=(20,10), pady=10)
        self.show_frame.grid(row=1, column=1, sticky="nsew", padx=(10,20), pady=10)

        self.list_frame.configure(padx=10, pady=10)
        self.show_frame.configure(padx=10, pady=10)

        self.option_add("*Font", "Arial 11")

    def run(self):
        self.mainloop()
