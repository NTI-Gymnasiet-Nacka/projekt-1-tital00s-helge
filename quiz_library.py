import tkinter as tk
from tkinter import messagebox
import csv

class QuizLibrary:
    def __init__(self, master, main_app):
        self.master = master
        self.main_app = main_app
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
            with open('quiz_library.csv', mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    quiz_name = row[0]
                    button = tk.Button(self.quiz_buttons_frame, text=quiz_name,
                                       command=lambda name=quiz_name: self.take_quiz(name))
                    button.pack()
        except FileNotFoundError:
            pass

    def take_quiz(self, quiz_name):
        try:
            with open('quiz_library.csv', mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if row[0] == quiz_name:
                        quiz_data = row[1:]
                        questions = []
                        for i in range(0, len(quiz_data), 3):
                            question = {'question': quiz_data[i], 'options': [{'text': quiz_data[i + 1], 'correct': bool(int(quiz_data[i + 2]))}]}
                            questions.append(question)

                        quiz_results = self.take_quiz_questions(questions)
                        messagebox.showinfo("Quiz App", f"Quiz Results for {quiz_name}:\nCorrect Answers: {quiz_results}")

        except FileNotFoundError:
            pass

    def take_quiz_questions(self, questions):
        correct_answers = 0

        for question in questions:
            user_answer = self.display_question(question['question'], question['options'])
            correct_answer = next((option['correct'] for option in question['options'] if option['text'] == user_answer), False)
            if correct_answer:
                correct_answers += 1

        return correct_answers

    def display_question(self, question_text, options):
        answer = simple_popup(question_text, [option['text'] for option in options])
        return answer

    def back_to_start_page(self):
        self.master.destroy()
        self.main_app.show_start_page()

def simple_popup(question, options):
    popup = tk.Toplevel()
    popup.title("Take Quiz")
    popup.geometry("400x300")

    tk.Label(popup, text=question).pack()

    user_answer = tk.StringVar()
    for option in options:
        tk.Radiobutton(popup, text=option, variable=user_answer, value=option).pack()

    tk.Button(popup, text="Submit", command=popup.destroy).pack()

    popup.wait_window()

    return user_answer.get()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizLibrary(root)
    root.mainloop()
