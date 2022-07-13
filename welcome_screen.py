from termcolor import colored


def welcome_screen():
    """
    Welcome screen for the game. \n
    Generated with: https://www.ascii-art-generator.org/
    """
    print("""

                   ____    _    _  _____   ______
                  / __ \  | |  | | |_  _| |___  /
                 | |  | | | |  | |  | |      / /
                 | |  | | | |  | |  | |     / /
                 | |__| | | |__| | _| |_   / /__ 
                  \___\_\  \____/ |_____| /_____|
    
    
    """)

    print("\n")
    print("Welcome to Quiz!\n")
    print("\n")
    global name
    while True:
        name = input("Enter your name:").capitalize()
        if not name.isalnum():
            print(colored("Not an appropriate input.", 'yellow'))
        else:
            break

    print(f"Let's start quiz, {name}!")
    print("\n")
    return name
