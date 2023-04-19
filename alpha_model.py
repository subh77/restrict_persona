import openai

openai.api_key = open('key.txt').read().strip('\n')

message_history = []

import pandas as pd

# df = pd.read_json("questions.json")


class AIMemory:
    def __init__(self):
        # self.user_input = input(">: ")
        self.df = pd.read_json("questions.json")
        print(self.df)
        self.df = self.df.to_json()
        # reply_content = cache_memory(user_input)
    def cache_memory(self):
        message_history = {"role":"user", "content":"I want you to behave as someone taking an interview for SD2 python developer. The candidate will submit the code snippets for the given questions. Your job is to grade each question and give a score ranging from 1 to 10, then grade the candidate on an overall percentage scale. If you find any escape sequences then remove those and then grade the candidate's code."}, {"role":"assistant", "content":"Sure, I can do that. Please provide me with the code snippets and the questions."}, {"role":"user", "content":self.df}
        # message_history.append({"role":"user", "content":self.user_input}, {"role":"assistant", "content":"Sure, I can do that. Please provide me with the code snippets and the questions."}, {"role":"user", "content":self.df})
        print(message_history)
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = message_history
            )
        # print(completion.choices[0].message.content)
        return completion.choices[0].message.content


# val = AIMemory().cache_memory()
# print(val)
# memory_continuity = input("Default is True, if you wanna close app then input False: ", True)
# while memory_continuity == True:
#     AIMemory().cache_memory