import json
import tkinter as tk
from tkinter import messagebox
import os

ques_path = os.path.abspath(__file__)
qes_dir = os.path.split(ques_path)[0]
rel_path = "questions.json"
abs_file_path = os.path.join(qes_dir, rel_path)
print(abs_file_path)

class QuestionWindow:
    def __init__(self, master):
        self.master = master
        self.current_question = 0
        self.questions = self.load_questions()

        self.question_label = tk.Label(master, text=self.questions[self.current_question]['ques'])
        self.question_label.pack()

        self.answer_entry = tk.Entry(master, width=50)
        self.answer_entry.pack(ipady=150)

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_answer)
        self.submit_button.pack()

    def load_questions(self):
        with open(abs_file_path, 'r') as f:
            questions = json.load(f)
        return questions

    def submit_answer(self):
        self.questions[self.current_question]['ans'] = self.answer_entry.get()

        with open(abs_file_path, 'w') as f:
            json.dump(self.questions, f)

        messagebox.showinfo("Success", "Answer submitted!")

        self.current_question += 1

        if self.current_question >= len(self.questions):
            self.master.destroy()
        else:
            self.question_label.configure(text=self.questions[self.current_question]['ques'])
            self.answer_entry.delete(0, tk.END)

root = tk.Tk()
root.geometry("500x500")
root.title("Questionnaire")
question_window = QuestionWindow(root)
root.mainloop()