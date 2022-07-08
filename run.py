def start_game():
    """
    Displays a question with a multiple answers
    and wait response from user
    """


answers = []
cor_answers = 0
choise_list = ['a', 'b', 'c', 'd']

question_set = {
        "1. The wind velocity is measured by which instrument?": "B",
        "2. The Red planet is called after which planet?": "B",
        "3. Name the highest mountain in Africa?": "C",
        "4. Which river is known to be the longest on earth?": "D",
        "5. Why was the Great Wall of China build for?": "B"
        }

for key, value in question_set.items():
    print("\n")
    print(key)

    while True:
        user_answer = input("Pick an answer from (A, B, C, or D): ")
        if user_answer.lower() not in choise_list:
            print("Not an appropriate choice.")
        else:
            break

    answers.append(user_answer)
print(answers)


game = start_game()

print(game)

# check_answer()
    #check user input
   
    
# count_cor_answers()
    #count correct user answers

# show_results()
    #print results for user

# new_game()
    #ask the user if he wants to play again
