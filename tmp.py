import json
import tkinter as tk
from tkinter import messagebox

class QuestionWindow:
    def __init__(self, master):
        self.master = master
        self.current_question = 0
        self.questions = self.load_questions()

        self.question_label = tk.Label(master, text=self.questions[self.current_question]['ques'])
        self.question_label.pack()

        self.answer_entry = tk.Entry(master, width=50)
        self.answer_entry.pack(ipady=150)
        self.answer_entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_answer)
        self.submit_button.pack()

    def load_questions(self):
        with open('questions.json', 'r') as f:
            questions = json.load(f)
        return questions

    def submit_answer(self):
        self.questions[self.current_question]['ans'] = self.answer_entry.get()

        with open('questions.json', 'w') as f:
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


# import json
# import tkinter as tk

# def save_answer():
#     global current_question
#     current_question['ans'] = answer.get("1.0", "end-1c")
#     with open('questions.json', 'w') as file:
#         json.dump(questions, file)
#     next_question()

# def next_question():
#     global current_question
#     if questions:
#         current_question = questions.pop(0)
#         question.config(text=current_question['ques'])
#         example.config(text=current_question['example'])
#         answer.delete("1.0", "end")
#     else:
#         root.destroy()

# with open('questions.json', 'r') as file:
#     questions = json.load(file)

# root = tk.Tk()
# root.geometry("500x400")
# root.title("Questionnaire")

# question = tk.Label(root, text="", font=("Arial", 14))
# question.pack(pady=10)

# example = tk.Label(root, text="", font=("Arial", 10))
# example.pack(pady=10)

# answer_label = tk.Label(root, text="Answer:", font=("Arial", 12))
# answer_label.pack(pady=10)

# answer = tk.Text(root, height=10)
# answer.pack()

# submit_button = tk.Button(root, text="Submit", command=save_answer)
# submit_button.pack(pady=10)

# current_question = None
# next_question()

# root.mainloop()
