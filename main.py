import tkinter as tk
from tkinter import messagebox
from create_quiz import QuizMaker
from quiz_library import QuizLibrary
import csv

class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz App")
        self.master.geometry("600x400")

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

    def create_quiz(self):
        quiz_maker_window = tk.Toplevel(self.master)
        QuizMaker(quiz_maker_window, self)

    def open_quiz_library(self):
        quiz_library_window = tk.Toplevel(self.master)
        QuizLibrary(quiz_library_window, self)

    def save_to_library(self, quiz_name, questions):
        with open('quiz_library.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([quiz_name, questions])

    def delete_quiz(self, quiz_name):
        messagebox.showinfo("Quiz App", "Quiz deleted.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
