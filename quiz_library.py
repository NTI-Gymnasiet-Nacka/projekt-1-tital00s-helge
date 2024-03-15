import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
from functools import partial

class QuizLibrary:
    def __init__(self, master, main_app, csv_file='quiz_library.csv'):
        self.master = master
        self.main_app = main_app
        self.csv_file = csv_file
        self.master.title("Quiz Library")
        self.master.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        self.label_library = tk.Label(self.master, text="Quiz Library")
        self.label_library.pack()

        self.quiz_buttons_frame = tk.Frame(self.master)
        self.quiz_buttons_frame.pack()

        self.load_quiz_buttons()

        self.button_back = tk.Button(self.master, text="Back to Start Page", command=self.back_to_start_page)
        self.button_back.pack()

    def load_quiz_buttons(self):
        try:
            with open(self.csv_file, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    quiz_name = row[0]
                    button = tk.Button(self.quiz_buttons_frame, text=quiz_name,
                                       command=partial(self.take_quiz, quiz_name))
                    button.pack()
        except FileNotFoundError:
            messagebox.showerror("Error", "Quiz library file not found.")

    def take_quiz(self, quiz_name):
        try:
            with open(self.csv_file, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if row[0] == quiz_name:
                        quiz_data = row[1:]  # Skip the quiz name
                        questions = self.parse_quiz_data(quiz_data)
                        quiz_results = self.take_quiz_questions(questions)
                        messagebox.showinfo("Quiz App", f"Quiz Results for {quiz_name}:\nCorrect Answers: {quiz_results}")
                        break
        except FileNotFoundError:
            messagebox.showerror("Error", "Quiz library file not found.")

    def parse_quiz_data(self, quiz_data):
        questions = []
        for i in range(0, len(quiz_data), 9):  # Adjust based on your actual CSV structure
            question_text = quiz_data[i]
            options = [{'text': quiz_data[i + j*2 + 1], 'correct': bool(int(quiz_data[i + j*2 + 2]))} for j in range(4)]
            questions.append({'question': question_text, 'options': options})
        return questions

    def take_quiz_questions(self, questions):
        correct_answers = 0
        for question in questions:
            user_answer = self.display_question(question['question'], question['options'])
            if user_answer:
                correct_answer = any(option['correct'] for option in question['options'] if option['text'] == user_answer)
                if correct_answer:
                    correct_answers += 1
        return correct_answers

    def display_question(self, question_text, options):
        popup = tk.Toplevel()
        popup.title("Take Quiz")
        popup.geometry("400x300")
        tk.Label(popup, text=question_text).pack()
        user_answer = simpledialog.askstring("Take Quiz", "Your Answer", parent=popup)
        popup.destroy()
        return user_answer

    def back_to_start_page(self):
        self.master.destroy()
        self.main_app.show_start_page()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizLibrary(root)
    root.mainloop()
