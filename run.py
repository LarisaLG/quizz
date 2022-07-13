from termcolor import colored

import welcome_screen


# Quiz questions
question_set = {
            "1. The wind velocity is measured by which instrument?": "B",
            "2. The Red planet is called after which planet?": "B",
            "3. Name the highest mountain in Africa?": "C",
            "4. Which river is known to be the longest on earth?": "D",
            "5. Why was the Great Wall of China build for?": "B"
            }

# Answer options for questions
answers_list = [
            "A. Barometer\nB. Anemometer\nC. Hygrometer\nD. Velocity meter\n",
            "A. Mercury\nB. Mars\nC. Jupiter\nD. Saturn\n",
            "A. Mount Kenya\nB. Mount Stanley\nC. Mount Kilimanjaro\n"
            "D. Atlas Mountains\n",
            "A. Niger River\nB. Lena River\nC. Congo River\nD. Nile River\n",
            "A. Trade route\nB. Protection against Mongolians and Invaders\n"
            "C. Practice place for the martial artists\nD. Tourism purposes\n"
        ]

answers = []
choise_list = ['a', 'b', 'c', 'd']


def start_game():
    """
    Displays a question with a multiple answers
    and wait response from user
    """
    cor_answers = 0

    for ind, key in enumerate(question_set):
        print("\n")
        print(key)
        print(answers_list[ind])
        while True:
            user_answer = input("Pick an answer from (A, B, C, or D): ")\
                .upper()
            if user_answer.lower() not in choise_list:
                print(colored("Not an appropriate choice.", 'yellow'))
            else:
                break

        answers.append(user_answer)

        answer = question_set.get(key)

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
    print("QUIZ RESULTS")
    print("\n")

    print(colored("Correct answers:", 'blue'))
    for key, val in question_set.items():
        print(val, end=' ')
    print("\n")

    print(colored("Your answers:", 'cyan'))
    print(' '.join(answers))
    print("\n")
    user_scores = int((cor_answers/len(question_set))*100)
    print(f"So, {(welcome_screen.name)} you answered {(user_scores)}% \
of the questions correctly")

    new_game()


def new_game():
    """
    Ask the user if he wants to play again
    """
    print("\n")

    if input("Do you want play again? (Y/N): ").upper() == "Y":
        answers.clear()
        start_game()
    else:
        print(f"Ok, thanks for playing!\n See you soon! Bye!")
        welcome_screen.welcome_screen()


def main():
    """
     Run all programm functions
    """
    welcome_screen.welcome_screen()
    start_game()


main()
