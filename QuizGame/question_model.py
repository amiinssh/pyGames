class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def check_answer(self, user_input):
        if user_input == self.answer:
            return "That was right!", 1
        else:
            return "That was false!", -1
