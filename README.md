# **Bulls and Calves**

Bulls and Calves is a Python terminal game that runs on Code Institute's mock terminal in Heroku.

This is a fun game in which the game generates a random 2, 3 or 4 digit number.

The player then chooses to guess the numbers in which the game prompts "bulls" or "calves" if the user guesses the numbers correctly or is partially correct. This will test the users problem solving skills and logical thinking.

![Image of the app](/assets/bull-and-calves-heroku.jpg)

### **[Click to visit the live version of Bulls and Calves](https://bulls-and-calves.herokuapp.com/)**

# ***Table of Contents***
- [User Experience (UX)](#user-experience-ux)
- [Design](#design)

# **User Experience (UX)**

### User Goals
- To be able to play the game without having to run into any errors.
- To be able to read and understand how to play the game.
- To have the option of different difficulties in order to make the game more challenging.
- To be able to record the users guesses and have it displayed in order to aid them in the game.
- To have the option of playing again and choosing a different difficulty if they'd like.
- To be able to see how many times the user beats the game after they finish playing.

### User Stories
- As a user, I would like to be able to play the game and choose a difficulty.
- As a user, I would like the option to restart the game after completing it.
- As a user, I would like to see how many times I guess the numbers correctly after finishing the game.

# **Design**
## Flow Chart
I created a flowchart by using [Lucid](https://lucid.co/) in order to map out what I wanted to happen in the terminal.

![Flowchart image](/assets/bulls-and-calves-flowchart.jpeg)

## Features
### Current features

*Starting screen*

![](/assets/game-start-screen.jpg)
- When the game starts up, it informs the user of what they are playing.
- It tells the user how to play the game.
- It also informs the user of the games difficulty levels.
- It prompts the user to enter their name.

*Choose difficulty*

![](/assets/choose-difficulty.jpg)
- After user inputs their name they are asked to choose difficulty by choosing to guess either 2, 3 or 4 digits.

*After choosing difficulty*

![](/assets/difficulty-chosen.jpg)
- After choosing difficulty, the program repeats the difficulty level chosen by the user. 
- The user must then input their guess.

*Playing Bulls and Calves*

![](/assets/no-bull-or-calf.jpg)
- The above is displayed if the user does not get any number correct.

![](/assets/0-bull-1-calf.jpg)
- The above is displayed if the user guess a correct number but in the wrong position.

![](/assets/1-bull-0-calf.jpg)
- The above is displayed if the user guesses a correct number and also in the correct position.

![](/assets/user-congrats.jpg)
- The above is displayed once the user guesses all the numbers correctly.
- The user is then asked if they would like to play again.

![](/assets/finish-game-display-results.jpg)
- If the user chooses not to play again after after guessing correctly, the program displays how many times they guessed correctly.

![](/assets/finish-game-play-again.jpg)
- If the user chooses to play again, they are redirected back to choose the difficulty and play again.

### Potential Future Improvements or Implementation
- Create an optional feature so that the user could play against a bot to guess the numbers also.
- Make the game more visually pleasing by including different colours and drawing the name of the game instead of just plain text.

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