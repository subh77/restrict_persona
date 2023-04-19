import openai

openai.api_key = open('key.txt').read().strip('\n')

message_history = []


class AIMemory:
    def __init__(self):
        pass
    def cache_memory(self):
        message_history.append({"role":"user", "content":self.user_input})
        print(message_history)
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = message_history
            )
        return completion.choices[0].message.content

    user_input = input(">: ")
    reply_content = cache_memory(user_input)
    print(reply_content)

memory_continuity = input("Default is True, if you wanna close app then input False: ", True)
while memory_continuity == True:
    AIMemory().cache_memory