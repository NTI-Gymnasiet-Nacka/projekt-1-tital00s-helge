import tkinter as tk
from tkinter import messagebox
from quiz_library import QuizLibrary
from create_quiz import QuizMaker
import csv

class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz App")
        self.master.geometry("800x600")

        with open('quiz_library.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Quiz Name', 'Question', 'Option 1', 'Correct 1', 'Option 2', 'Correct 2', 'Option 3', 'Correct 3', 'Option 4', 'Correct 4'])

        self.show_start_page()

    def show_start_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        self.label_welcome = tk.Label(self.master, text="Welcome to Quiz App!")
        self.label_welcome.pack()

        self.button_create_quiz = tk.Button(self.master, text="Create Quiz", command=self.create_quiz)
        self.button_create_quiz.pack()

        self.button_quiz_library = tk.Button(self.master, text="Quiz Library", command=self.open_quiz_library)
        self.button_quiz_library.pack()

        self.button_exit = tk.Button(self.master, text="Exit", command=self.exit_app)
        self.button_exit.pack()

    def create_quiz(self):
        quiz_maker_window = tk.Toplevel(self.master)
        QuizMaker(quiz_maker_window, self)

    def open_quiz_library(self):
        quiz_library_window = tk.Toplevel(self.master)
        QuizLibrary(quiz_library_window, self)

    def exit_app(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
