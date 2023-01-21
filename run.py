import random

# NUMBERS const will be used to generate the game code
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# random.sample to generate random unique numbers
def generate_code(code_length):
    return random.sample(NUMBERS, code_length)


def validate_game_difficulty(game_difficulty):
    if game_difficulty in [2, 3, 4]:
        return True
    return False


def main():
    print("Welcome to Bulls and Calves!\n")
    print("***How To Play***\nGuess the right number!\nIf a number is one of the correct digits and is in the correct position, it's a bull.\nIf a number is one of the correct digits but is in the incorrect position, it's a calf.\n")
    player_name = input("Please enter your name: ")
    print(f"Hello {player_name}, please make sure to read the instructions to know how to play!\n")
    print("Choose your difficulty - How many digits would you like to guess? ")
    
    # Validate difficulty set by user - Keep prompting user until they provide one of the expected difficulties.
    valid_difficulty = False
    while not valid_difficulty:
        difficulty_level = input("Options are 2, 3 or 4\n")
        valid_difficulty = validate_game_difficulty(int(difficulty_level))
        # Check if the game difficulty provided is not valid and if not send a message to choose one of the options
        if not valid_difficulty:
            print("You provided an invalid game difficulty - please choose one of the options below")


    # This will generate a random code used by the game
    game_code = generate_code(int(difficulty_level))


    user_input = input("Enter your guess: ")
    print(user_input)


main()