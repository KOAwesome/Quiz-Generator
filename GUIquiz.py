import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import random
import docx

class QuizApplication(tk.Tk):
    def __init__(self, quiz_path):
        super().__init__()
        self.title("Quiz Application")
        self.geometry("600x400")

        self.quiz = self.load_quiz(quiz_path)
        self.total_questions = len(self.quiz)
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(self, text="Question")
        self.question_label.pack(pady=10)

        self.question_text = ScrolledText(self, height=6, width=60)
        self.question_text.pack()

        self.options_label = tk.Label(self, text="Options")
        self.options_label.pack(pady=10)

        self.option_buttons = []
        for _ in range(4):
            option_button = tk.Button(self, text="", width=40, command=lambda: self.check_answer(option_button))
            option_button.pack(pady=5)
            self.option_buttons.append(option_button)

        self.next_button = tk.Button(self, text="Next", width=20, command=self.next_question)
        self.next_button.pack(pady=10)

        self.show_question()

    def load_quiz(self, quiz_path):
        doc = docx.Document(quiz_path)
        quiz = []
        table = doc.tables[0]

        for row in table.rows[1:]:
            question = row.cells[1].text.strip()
            options = [cell.text.strip() for cell in row.cells[3:7]]
            answer = row.cells[7].text.strip()

            quiz.append({"question": question, "options": options, "answer": answer})

        random.shuffle(quiz)
        return quiz

    def show_question(self):
        question = self.quiz[self.current_question]
        self.question_label.config(text=f"Question {self.current_question + 1}/{self.total_questions}")
        self.question_text.delete(1.0, tk.END)
        self.question_text.insert(tk.END, question["question"])

        options = question["options"]
        random.shuffle(options)

        for i, option in enumerate(options):
            self.option_buttons[i].config(text=option)

        self.next_button.config(state=tk.DISABLED)

    def check_answer(self, option_button):
        question = self.quiz[self.current_question]
        user_answer = option_button["text"]

        if user_answer == question["answer"]:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", f"Your answer is incorrect! The correct answer is {question['answer']}")

        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1

        if self.current_question >= self.total_questions:
            self.show_result()
        else:
            self.show_question()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"Quiz completed! Your score: {self.score}/{self.total_questions}")
        self.quit()


# Example usage
quiz_path = "yourworddocument.docx"  # Replace with the correct path to your Word document
app = QuizApplication(quiz_path)
app.mainloop()
