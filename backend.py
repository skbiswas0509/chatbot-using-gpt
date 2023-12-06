import openai

class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = user_input,
            max_tokens = 3000,
            temperature = 0.5,
        ).choices[0].text
        return response

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("what is sun?")
    print(response)