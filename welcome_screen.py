def welcome_screen():
    """
    Welcome screen for the game. Generated with: https://www.ascii-art-generator.org/
    """
    print( """
                    ____  _    _ _____ ______   ____  _    _ ______  _____ _______ 
                  / __ \| |  | |_   _|___  /   / __ \| |  | |  ____|/ ____|__   __|
                 | |  | | |  | | | |    / /   | |  | | |  | | |__  | (___    | |   
                 | |  | | |  | | | |   / /    | |  | | |  | |  __|  \___ \   | |   
                 | |__| | |__| |_| |_ / /__   | |__| | |__| | |____ ____) |  | |   
                  \___\_\\____/|_____/_____|    \___\_\ ____/|______|_____/   |_|

  
    """ )



    print("\n")
    print("Welcome to Quiz!\n")
    global name
    name = input("Enter your name:").capitalize()
    print(f"Let's start quiz, {name}!")
    print("\n")
    return name
