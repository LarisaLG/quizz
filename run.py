"""
Import necessary modules and scripts
"""
import os
from termcolor import colored
import welcome_screen
import questions


answers = []
choise_list = ['a', 'b', 'c', 'd']


def start_game():
    """
    Displays a question with a multiple answers
    and wait response from user
    """
    cor_answers = 0

    for ind, key in enumerate(questions.question_set):
        print("\n")
        print(colored(key, 'cyan'))
        print(questions.answers_list[ind])
        while True:
            user_answer = input("Pick an answer from (A, B, C, or D): ")\
                .upper()
            if user_answer.lower() not in choise_list:
                print(colored("Not an appropriate choice.", 'yellow'))
            else:
                break

        answers.append(user_answer)

        answer = questions.question_set.get(key)

        cor_answers += check_answer(answer, user_answer)

    show_results(cor_answers, answers)


def check_answer(answer, user_answer):
    """
    Checks if user input is correct and counts correct answers
    """
    if answer == user_answer:
        print(colored("CORRECT ANSWER!", 'green'))
        return 1

    else:
        print(colored("YOU'RE WRONG!", 'red'))
        return 0


def show_results(cor_answers, answers):
    """
    displays quiz results and user given results
    """
    print("\n")
    print("************************")
    print("QUIZ RESULTS")
    print("************************")

    print(colored("Correct answers:", 'green'))
    for key, val in questions.question_set.items():
        print(val, end=' ')
    print("\n")

    print(colored("Your answers:", 'cyan'))
    print(' '.join(answers))
    print("\n")

    user_scores = int((cor_answers/len(questions.question_set))*100)
    print(colored(f"So, {(welcome_screen.name)} you answered {(user_scores)}% \
of the questions correctly", 'cyan'))
    print(colored(f"Number of correct answers is: {(cor_answers)} / {(len(questions.question_set))}", 'cyan'))
    
    new_game()


def new_game():
    """
    Ask the user if he wants to play again
    """
    print("\n")

    if input("Do you want play again? (Y/N): ").upper() == "Y":
        print("\n")
        answers.clear()
        start_game()
    else:
        print("\n")
        print(f"Ok, thanks for playing!\nSee you soon! Bye!")
        time.sleep(5)
        os.system('clear')


def main():
    """
     Run all programm functions
    """
    welcome_screen.welcome_screen()
    start_game()


main()
