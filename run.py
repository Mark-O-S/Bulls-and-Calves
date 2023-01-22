import random

"""NUMBERS const will be used to help generate the game code."""
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def generate_game_code(code_length):
    """
    This function is used to generate the code for the game.
    random.sample is used to generate unique random numbers that 
    the user will try to guess to win the game.
    """ 
    return random.sample(NUMBERS, code_length)


def validate_game_difficulty(game_difficulty):
    """
    This function will validate the game in any chosen difficulty.
    """
    if game_difficulty in ["2", "3", "4"]:
        return True
    return False


def validate_user_code_guess(user_code_guess, code_length):
    """
    This function will validate the user guess by checking that the users input are
    unique numbers between 0 - 9.
    """

    # Checks that each input is not a digit and is a negative.
    for digit in user_code_guess:
        if not digit.isdigit():
            return False

        if int(digit) < 0:
            return False

    # Using set function to ensure uniqueness of a number and so that they cannot reuse the same number.
    if len(set(user_code_guess)) != code_length:
        return False
    
    return True
    

def check_for_bull_or_calf(list_user_input, game_code):
    """
    This will check if the user input contains a bull or a calf.
    """
    # counters for bulls and calves 
    bulls = 0
    calves = 0
    
    # Loop through the indices of the user input list and ensure user inputs are converted as integers.
    for index in range(len(list_user_input)):
        if int(list_user_input[index]) in game_code:
            if int(list_user_input[index]) == game_code[index]:
                bulls += 1
            else:
                calves += 1
    
    print(f"You got {bulls} bulls and {calves} calves! ")
    if bulls == (len(list_user_input)):
        return True

    return False

"""
Allows the program to accept different types of 'yes' responses.
"""
yeslist = ["yes", "y", "ya", "ye", "yeah", "yep"]


def main():
    """
    This is the main function that executes the program.
    """
    print("-----------------------------")
    print("WELCOME TO BULLS AND CALVES!")
    print("-----------------------------")
    print("***HOW TO PLAY***\nGuess the right code!\nNote that you can only guess unique numbers from 0 - 9.")
    print("Numbers cannot be repeated each time you enter a guess, for example: entering '111' or '121' will be invalid.")
    print("If a number is one of the correct digits and is in the correct position, it's a bull.")
    print("If a number is one of the correct digits but is in the incorrect position, it's a calf.")
    print("Once you guess all Bull's you win the game!\n")
    player_name = input("Please enter your name: ")
    print(f"Hello {player_name}! Choose your difficulty below - How many digits would you like to guess?\n")

    player_wins = 0
    
    while True:

        # Validate difficulty set by user - Keep prompting user until they provide one of the expected difficulties.
        valid_difficulty = False
        while not valid_difficulty:
            difficulty_level = input("Options are 2, 3 or 4\n")
            valid_difficulty = validate_game_difficulty(difficulty_level)

            # Check if the game difficulty provided is not valid and if not send a message to choose one of the options.
            if not valid_difficulty:
                print("You provided an invalid game difficulty - please choose one of the options below:")
        
            if valid_difficulty:
                difficulty_level = int(difficulty_level)
                print(f"You have chosen difficulty level: {difficulty_level} digits.\nGood luck!")
    
        """
        This will generate a random code used by the game
        """
        game_code = generate_game_code(difficulty_level)
 

        # Create while loop to keep the user guessing until they guess the game code correctly.
        guessing_game_code = False
        while not guessing_game_code:
            user_input = input("\nEnter your guess: ")
            list_user_input = list(user_input)
            valid_user_code_guess = validate_user_code_guess(list_user_input, difficulty_level)

            # If the user_code_guess is not valid.
            if not valid_user_code_guess:
                print(f"Invalid guess, please enter a {difficulty_level} digit unique number")
        
            # if the user code guess is valid.
            else:
                check_bulls_calves = check_for_bull_or_calf(list_user_input, game_code)
                if check_bulls_calves:
                    player_wins += 1
                    guessing_game_code = True
        print(f"\nCongratulations {player_name}! You guessed all the numbers correctly!!!\n")


        restart = input("Would you like to play again?\nIf so, type 'Yes'. If not, type any other word: ").lower()
        if restart in yeslist:
            guessing_game_code = True
        else:
            print(f"Thank you for playing {player_name}. You guessed correctly {player_wins} times!")
            exit()

if __name__ == '__main__':
    main()