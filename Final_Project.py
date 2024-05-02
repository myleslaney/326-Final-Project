import random

"""Create a questions class"""
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

"""Create quiz class here and define the methods"""
class Quiz:
    def __init__(self, subject):
        self.subject = subject
        self.questions = []

    def add_question(self, question, answer):
        self.questions.append((question, answer))

    def run_quiz(self):
        random.shuffle(self.questions)
        num_questions = len(self.questions)
        correct_answers = 0
        
        print(f"--- {self.subject} Quiz ---")
        
        for question, answer in self.questions:
            print(question)
            user_answer = input("Input your answer here: ")
            if user_answer.lower() == answer.lower():
                print("Correct!")
                correct_answers += 1
            else:
                print(f"Wrong! The correct answer is {answer}")

        percentage_score = (correct_answers / num_questions) * 100
        print(f"\nYou got {correct_answers} out of {num_questions} questions correct.")
        print(f"Your percentage score is: {percentage_score:.2f}%")
"""A unit test will be taken for the question and quiz classes and will be in a separate file"""


"""Make some sample data to input for the quizzes with different themes"""

def sample_quizzes():
    math_quiz = Quiz("Math")
    math_quiz.add_question("How many degrees does a triangle have?", "180")
    math_quiz.add_question("Square root of 25?", "5")
    math_quiz.add_question("9*9?", "81")
    math_quiz.add_question("How many sides does a pentagon have?", "5")
    math_quiz.add_question("What are the first 3 digits of pi?", "3.14")

    history_quiz = Quiz("History")
    history_quiz.add_question("What year was the University of Maryland founded?", "1856")
    history_quiz.add_question("Which empire was Julius Caesar part of?", "Roman Empire")
    history_quiz.add_question("When was the U.S founded?", "1776")
    history_quiz.add_question("What year did WW2 end?", "1945")
    history_quiz.add_question("Who 'discovered' the Americas?", "Christopher Columbus")

    science_quiz = Quiz("Science")
    science_quiz.add_question("What is the name of gold on the periodic table?", "AU")
    science_quiz.add_question("What is the molecular name of water?", "H2O")
    science_quiz.add_question("What is the process of which plants 'eat'?", "Photosynthesis")
    science_quiz.add_question("What is the center of an Atom called?", "Nucleus")
    science_quiz.add_question("What is the name of our galaxy?", "Milky Way")

    geography_quiz = Quiz("Geography")
    geography_quiz.add_question("What continent is the U.S.A located in?", "North America")
    geography_quiz.add_question("How many continents are there?", "7")
    geography_quiz.add_question("How many oceans are there?", "5")
    geography_quiz.add_question("As of 2024, what is the most populated country?", "India")
    geography_quiz.add_question("What is the largest country by land area?", "Russia")

    return math_quiz, history_quiz, science_quiz, geography_quiz

"""Create Main function here"""
def main():
    print("Welcome to the Quiz App!")
    print("Choose a quiz:")
    print("1. Math")
    print("2. Science")
    print("3. History")
    print("4. Geography")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        math_quiz = sample_quizzes()[0]
        math_quiz.run_quiz()
    elif choice == "2":
        science_quiz = sample_quizzes()[2]
        science_quiz.run_quiz()
    elif choice == "3":
        history_quiz = sample_quizzes()[1]
        history_quiz.run_quiz()
    elif choice == "4":
        geography_quiz = sample_quizzes()[3]
        geography_quiz.run_quiz()
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

"""Pass the main function to if__name__ statement"""
if __name__ == "__main__":
    main()
