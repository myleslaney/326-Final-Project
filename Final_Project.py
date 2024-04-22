

"""Create quiz class here and define the methods"""
class Quiz:
    def __init__(self, subject):
        self.subject = subject
        self.questions = {}

    def add_question(self, question, answer):
        self.questions[question] = answer

    def take_quiz(self):
        questions = list(self.questions.items())
        random.shuffle(questions)
        for question, answer in questions:
            print(question)
            user_answer = input("Input your answer here: ")
            if user_answer.lower() == answer.lower():
                print("Correct!")
            else:
                print(f"Wrong! The correct answer is {answer}")

"""A unit test will be taken here to test that the code created a successful instance of the quiz class"""



"""Make some sample data to input for the quizzes with different themes"""

def sample_quizzes():
    math_quiz = Quiz("Math")
    math_quiz.add_question("How many degrees does a triangle have?", "180")
    math_quiz.add_question("Square root of 25?", "5")

    history_quiz = Quiz("History")
    history_quiz.add_question("What year was the University of Maryland founded?", "1856")

    science_quiz = Quiz("Science")
    science_quiz.add_question("What is the name of gold on the periodic table?", "AU")

    return math_quiz, history_quiz, science_quiz

"""Create Main function here"""
def main():





"""Pass the main function to if__name__ statement"""
if __name__ == "__main__":
    main()
