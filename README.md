What went wrong:
When attempting to generate 3 unique digits, I called the random module directly.
I received "TypeError: 'module' object is not callable"
To fix this, I used random.sample() function to generate unique numbers for the game.

When I wanted to use a list of strings, I was still using the input I got from the user. I expected a list of strings but instead I got a string.
user_input = input("Enter your guess: ")
list_user_input = list(user_input)
valid_user_code = validate_user_code_guess(user_input, difficulty_level)