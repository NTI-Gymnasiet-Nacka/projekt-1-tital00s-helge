import tkinter as tk
from tkinter import messagebox

class QuizMaker:
    def __init__(self, master, main_app):
        self.master = master
        self.main_app = main_app
        self.master.title("Create Quiz")

        self.quiz_name = tk.StringVar()
        self.questions = []

        self.create_widgets()

    def create_widgets(self):
        self.label_quiz_name = tk.Label(self.master, text="Enter Quiz Name:")
        self.entry_quiz_name = tk.Entry(self.master, textvariable=self.quiz_name)
        self.label_quiz_name.pack()
        self.entry_quiz_name.pack()

        self.label_question = tk.Label(self.master, text="Question:")
        self.entry_question = tk.Entry(self.master)
        self.label_question.pack()
        self.entry_question.pack()

        self.options = []
        for i in range(4):
            option_label = tk.Label(self.master, text=f"Option {chr(65 + i)}:")
            option_entry = tk.Entry(self.master)
            option_label.pack()
            option_entry.pack()
            self.options.append(option_entry)

        self.button_add_question = tk.Button(self.master, text="Add Question", command=self.add_question)
        self.button_add_question.pack()

        self.button_finish_quiz = tk.Button(self.master, text="Finish Quiz", command=self.finish_quiz)
        self.button_finish_quiz.pack()

        self.button_delete_quiz = tk.Button(self.master, text="Delete Quiz", command=self.delete_quiz)
        self.button_delete_quiz.pack()

        self.button_back = tk.Button(self.master, text="Back to Start Page", command=self.back_to_start_page)
        self.button_back.pack()

    def add_question(self):
        question_text = self.entry_question.get()
        options_text = [entry.get() for entry in self.options]

        if not question_text or not any(options_text):
            messagebox.showerror("Error", "Question and options cannot be empty.")
            return

        question_data = {
            'question': question_text,
            'options': options_text
        }
        self.questions.append(question_data)

        messagebox.showinfo("Quiz App", "Question added successfully!")
        self.entry_question.delete(0, tk.END)
        for entry in self.options:
            entry.delete(0, tk.END)

    def finish_quiz(self):
        if not self.quiz_name.get() or not self.questions:
            messagebox.showerror("Error", "Quiz name and questions are required.")
            return

        self.main_app.save_to_library(self.quiz_name.get(), self.questions)
        messagebox.showinfo("Quiz App", "Quiz finished!\nSaved to the library.")
        self.back_to_start_page()

    def delete_quiz(self):
        self.main_app.delete_quiz(self.quiz_name.get())
        messagebox.showinfo("Quiz App", "Quiz deleted.")
        self.back_to_start_page()

    def back_to_start_page(self):
        self.master.destroy()
        self.main_app.show_start_page()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizMaker(root)
    root.mainloop()
