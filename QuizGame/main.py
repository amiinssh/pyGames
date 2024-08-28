import random
from data import question_data
from question_model import Question

class Game:
    def __init__(self):
        self.user_score = 0
        self.game_running = True
        self.questions = [Question(q["text"], q["answer"]) for q in question_data]

    def select_random_question(self):
        return random.choice(self.questions)

    def play(self):
        while self.game_running:
            random_question = self.select_random_question()
            print(f"Question: {random_question.text}")
            user_input = input("True or False?: ")
            result, score_change = random_question.check_answer(user_input)
            self.user_score += score_change
            print(result)
            print(f"Your score: {self.user_score}")

            if self.user_score <= 0:
                self.game_running = False

        print("Game Over! Your score reached zero.")

if __name__ == "__main__":
    game = Game()
    game.play()
