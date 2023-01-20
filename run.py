

def main():
    print("Welcome to Bulls and Calves!\n")
    print("***How To Play***\nGuess the right number!\nIf a number is one of the correct digits and is in the correct position, it's a bull.\nIf a number is one of the correct digits but is in the incorrect position, it's a calf.\n")
    player_name = input("Please enter your name: ")
    print(f"Hello {player_name}, please make sure to read the instructions to know how to play!")


    user_input = input("Enter your guess: ")
    print(user_input)


main()