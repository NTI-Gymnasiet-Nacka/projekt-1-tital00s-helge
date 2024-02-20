import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz App")

        self.quiz_name = tk.StringVar()
        self.questions = []

        self.create_widgets()

    def create_widgets(self):
        self.label_quiz_name = tk.Label(self.master, text="Enter Quiz Name:")
        self.entry_quiz_name = tk.Entry(self.master, textvariable=self.quiz_name)
        self.label_quiz_name.pack()
        self.entry_quiz_name.pack()

        self.button_create_quiz = tk.Button(self.master, text="Create Quiz", command=self.start_creating_quiz)
        self.button_create_quiz.pack()

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

    def start_creating_quiz(self):
        self.quiz_name.set("")
        self.questions = []
        messagebox.showinfo("Quiz App", "Quiz creation started!")

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

        messagebox.showinfo("Quiz App", "Quiz finished!\nYou can save it to the library or go back to create a new one.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
