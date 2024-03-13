import tkinter as tk
from tkinter import messagebox
import csv

class QuizMaker:
    def __init__(self, master, main_app):
        self.master = master
        self.main_app = main_app
        self.master.title("Create Quiz")
        self.master.geometry("600x400")

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

        self.options_frame = tk.Frame(self.master)
        self.options_frame.pack()

        self.options = []
        self.correct_checkboxes = []
        for i in range(4):
            option_label = tk.Label(self.options_frame, text=f"Option {chr(65 + i)}:")
            option_entry = tk.Entry(self.options_frame)
            correct_var = tk.BooleanVar()
            correct_checkbox = tk.Checkbutton(self.options_frame, variable=correct_var)

            option_label.grid(row=i, column=0, sticky=tk.E)
            option_entry.grid(row=i, column=1)
            correct_checkbox.grid(row=i, column=2, sticky=tk.W)

            self.options.append(option_entry)
            self.correct_checkboxes.append(correct_var)

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
        correct_answers = [var.get() for var in self.correct_checkboxes]

        if not question_text or not any(options_text):
            messagebox.showerror("Error", "Question and options cannot be empty.")
            return

        question_data = {
            'question': question_text,
            'options': [{'text': text, 'correct': correct} for text, correct in zip(options_text, correct_answers)]
        }
        self.questions.append(question_data)

        messagebox.showinfo("Quiz App", "Question added successfully!")
        self.entry_question.delete(0, tk.END)
        for entry in self.options:
            entry.delete(0, tk.END)
        for checkbox in self.correct_checkboxes:
            checkbox.set(0)

    def finish_quiz(self):
        if not self.quiz_name.get() or not self.questions:
            messagebox.showerror("Error", "Quiz name and questions are required.")
            return

        if not any(var.get() for var in self.correct_checkboxes):
            messagebox.showerror("Error", "At least one correct answer is required.")
            return

        try:
            with open('quiz_library.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                for question in self.questions:
                    row = [self.quiz_name.get(), question['question']]
                    row.extend([option['text'] for option in question['options']])
                    row.extend([int(option['correct']) for option in question['options']])
                    writer.writerow(row)

            messagebox.showinfo("Quiz App", "Quiz finished!\nSaved to the library.")
            self.back_to_start_page()

        except FileNotFoundError:
            pass

    def delete_quiz(self):
        try:
            with open('quiz_library.csv', mode='r') as file:
                reader = tk.reader(file)
                rows = list(reader)

            with open('quiz_library.csv', mode='w', newline='') as file:
                writer = tk.writer(file)
                for row in rows:
                    if row[0] != self.quiz_name.get():
                        writer.writerow(row)

            messagebox.showinfo("Quiz App", "Quiz deleted.")
            self.back_to_start_page()

        except FileNotFoundError:
            pass

    def back_to_start_page(self):
        self.master.destroy()
        self.main_app.show_start_page()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizMaker(root)
    root.mainloop()
