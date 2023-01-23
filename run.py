import random

# NUMBERS const will be used to help generate the game code.
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Allows the program to accept different types of 'yes' responses.
YESLIST = ["yes", "y", "ya", "ye", "yeah", "yep"]


def generate_game_code(code_length):
    """
    This is used to generate the code for the game.
    random.sample is used to generate unique random numbers that
    the user will try to guess to win the game.
    """
    return random.sample(NUMBERS, code_length)


def validate_game_difficulty(game_difficulty):
    """
    Validates the game in any chosen difficulty.
    """
    if game_difficulty in ["2", "3", "4"]:
        return True
    return False


def validate_user_code_guess(user_code_guess, code_length):
    """
    This function will validate the user guess by checking that the
    users input are unique numbers between 0 - 9.
    """

    # Checks that each input is not a digit and is a negative.
    for digit in user_code_guess:
        if not digit.isdigit():
            return False

        if int(digit) < 0:
            return False

    # Using set function to ensure a unique number is inputted.
    if len(set(user_code_guess)) != code_length:
        return False

    return True


def check_for_bull_or_calf(list_user_input, game_code):
    """
    This will check if the user input contains a bull or a calf.
    """
    # Counters for bulls and calves
    bulls = 0
    calves = 0
    # Loop through indices and ensure user inputs are converted to integers.
    for index, item in enumerate(list_user_input):
        if int(item) in game_code:
            if int(item) == game_code[index]:
                bulls += 1
            else:
                calves += 1
    print(f"You got {bulls} bulls and {calves} calves! ")
    if bulls == (len(list_user_input)):
        return True

    return False


def main():
    """
    This is the main function that executes the program.
    """
    print("-----------------------------")
    print("WELCOME TO BULLS AND CALVES!")
    print("-----------------------------")
    print(
        "***HOW TO PLAY***\nGuess the right code!"
    )
    print("Note that you can only guess unique numbers from 0 - 9.")
    print(
        "Numbers cannot be repeated each time you enter a guess, for example:"
    )
    print("Entering '111' or '121' will be invalid.")
    print(
        "If a number is one of the correct digits and in the correct position:"
    )
    print("It's a bull.")
    print(
        "If a number is one of the correct digits but incorrect position:"
    )
    print("It's a calf.")
    print(
        "The difficulty level is gauged by how many digits you are guessing."
    )
    print(
        "2 digits being the easiest and 4 digits being the hardest."
        )
    print("Once you guess all Bull's you win the game!\n")

    player_name = input("Please enter your name: ")

    print(f"\nHello {player_name}! Please choose your level of difficulty:\n")

    player_wins = 0
    while True:

        # Validate difficulty set by user - Keep prompting user until they
        # provide one of the expected difficulties.
        valid_difficulty = False
        while not valid_difficulty:

            difficulty_level = input(
                "Would you like to guess 2, 3 or 4 digits?\n"
                )

            valid_difficulty = validate_game_difficulty(difficulty_level)

            # Check if the game difficulty provided is not valid and if not
            # send a message to choose one of the options.
            if not valid_difficulty:
                print(
                    "You provided an invalid game difficulty - "
                    "please choose one of the options below:"
                )
            if valid_difficulty:
                difficulty_level = int(difficulty_level)
                print(
                    f"You have chosen difficulty level: {difficulty_level} "
                    "digits."
                )
                print("Good luck!")
        # This will generate a random code used by the game
        game_code = generate_game_code(difficulty_level)

        # Create while loop to keep the user guessing until
        # they guess the game code correctly.
        guessing_game_code = False
        while not guessing_game_code:

            user_input = input("\nEnter your guess: ")

            list_user_input = list(user_input)
            valid_user_code_guess = validate_user_code_guess(
                list_user_input, difficulty_level
            )

            # If the user_code_guess is not valid.
            if not valid_user_code_guess:
                print(
                    f"Invalid guess, please enter a {difficulty_level} digit"
                    " unique number"
                )
            # if the user code guess is valid.
            else:
                check_bulls_calves = check_for_bull_or_calf(list_user_input, game_code)
                if check_bulls_calves:
                    player_wins += 1
                    guessing_game_code = True
        print(
            f"\nCongratulations {player_name}! You guessed all the"
            " numbers correctly!!!\n"
        )

        restart = input(
            "Would you like to play again?\nIf so, type 'Yes'. "
            "If not, type any other word: "
        ).lower()

        if restart in YESLIST:
            guessing_game_code = True
        else:
            print(
                f"Thank you for playing {player_name}. "
                f"You guessed correctly {player_wins} times!"
            )
            exit()


if __name__ == "__main__":
    main()