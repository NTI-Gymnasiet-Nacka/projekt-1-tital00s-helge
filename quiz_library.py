import tkinter as tk
from tkinter import messagebox

class QuizLibrary:
    def __init__(self, master, main_app):
        self.master = master
        self.main_app = main_app
        self.master.title("Quiz Library")

        self.create_widgets()

    def create_widgets(self):
        self.label_library = tk.Label(self.master, text="Quiz Library")
        self.label_library.pack()

        self.button_back = tk.Button(self.master, text="Back to Start Page", command=self.back_to_start_page)
        self.button_back.pack()

    def back_to_start_page(self):
        self.master.destroy()
        self.main_app.show_start_page()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizLibrary(root)
    root.mainloop()