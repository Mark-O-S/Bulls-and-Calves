# Bulls and Calves

Bulls and Calves is a Python terminal game that runs on Code Institute's mock terminal in Heroku.

This is a fun game in which the game generates a random 2, 3 or 4 digit number, depending on their chosen difficulty.
The player then chooses to guess the numbers in which the game prompts "bulls" or "calves" if the user guesses the numbers correctly or is partially correct. This will test the users problem solving skills and logical thinking.

[Live version of Bulls and Calves game](https://bulls-and-calves.herokuapp.com/)

What went wrong:

When attempting to generate 3 unique digits, I called the random module directly.
I received "TypeError: 'module' object is not callable"
To fix this, I used random.sample() function to generate unique numbers for the game.

When I wanted to use a list of strings, I was still using the input I got from the user. I expected a list of strings but instead I got a string.
user_input = input("Enter your guess: ")
list_user_input = list(user_input)
valid_user_code = validate_user_code_guess(user_input, difficulty_level)

Was trying to compare two interger types when thet were an integer and a string. The string was an input from the user and wasn't converted to an integer type. Fixed the issue by using the int() function to then convert the value to an integer type.

I had an issue with validating the game difficulty from 116 - 22 and line 94 - 105. The issue was when the game requests to input difficulty, if the user inputs a word or a letter, it should print out (...invalid game difficulty). However, there is a ValueError instead. The program is looking for an integer number of 2, 3 or 4. I updated it so that the program will accept 2, 3 or 4 as a string if the user enters either of this number. After implementing the new code. The game works.