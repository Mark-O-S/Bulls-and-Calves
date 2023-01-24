# **Bulls and Calves**

Bulls and Calves is a Python terminal game that runs on Code Institute's mock terminal in Heroku.

This is a fun game in which the game generates a random 2, 3 or 4 digit number.

The player then chooses to guess the numbers in which the game prompts "bulls" or "calves" if the user guesses the numbers correctly or is partially correct. This will test the users problem solving skills and logical thinking.

![Image of the app](/assets/bull-and-calves-heroku.jpg)

### **[Click to visit the live version of Bulls and Calves](https://bulls-and-calves.herokuapp.com/)**

# ***Table of Contents***
- [User Experience (UX)](#user-experience-ux)
- [Design](#design)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)



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

### *Starting screen*

![](/assets/game-start-screen.jpg)
- When the game starts up, it informs the user of what they are playing.
- It tells the user how to play the game.
- It also informs the user of the games difficulty levels.
- It prompts the user to enter their name.

### *Choose difficulty*

![](/assets/choose-difficulty.jpg)
- After user inputs their name they are asked to choose difficulty by choosing to guess either 2, 3 or 4 digits.

### *After choosing difficulty*

![](/assets/difficulty-chosen.jpg)
- After choosing difficulty, the program repeats the difficulty level chosen by the user. 
- The user must then input their guess.

### *Playing Bulls and Calves*

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

**[Back to Table of Contents](#table-of-contents)**

# Technologies Used 
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - For building the game.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Generated from the python essentials template created by Code Institute.
- [HTML5](https://en.wikipedia.org/wiki/HTML5) - Generated from the python essential template built by Code Institute.
- [Github](https://github.com) - To save and store all the files of the site.
- [Gitpod](https://www.gitpod.io) - To write all the python. Also used to write the README.
- [CI Github template](https://github.com/Code-Institute-Org/python-essentials-template) - Used to help create the terminal that displays for users on the live page.
- [Code Beautify](https://codebeautify.org/python-formatter-beautifier) - To aid me in formatting my Python code.

**[Back to Table of Contents](#table-of-contents)**

# Testing

## Manual Testing

### Features

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|--------------|-------------
Write name and press enter | Receive a message "Hello {name}! Please choose difficulty" and ask how many digits the user wants to guess | As expected | Pass
When the user chooses either 2, 3 or 4 and press enter | The game repeats the users chosen difficulty and prompts user to enter guess | As expected | Pass
User enters a numbered guess | The game will respond and inform the user the result of their guess | As expected | Pass
Player get all digits correct | User is congratulated and asks if they want to play again | As expected | Pass
After guessing the numbers correctly, user chooses to play again | The user is prompted to choose the difficulty again and then continue the next round of guessing | As expected | Pass
After guessing the numbers correctly and not choosing to play again | The game thanks the user and displays how many times they guessed the numbers correctly | As expected | Pass

### Invalid Inputs

Input | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|--------------|-------------
When promted to choose difficulty, input a letter, word, symbol and any number besides 2, 3 or 4 | Receive a message saying "invalid game difficulty" and prompt user to select from 2, 3 or 4 | As expected | Pass
When prompted to enter users guess, input letters, words, symbols and more digits than required | Receive a message saying "Invalid guess" and the game tells user to input a unique number | As expected | Pass

### Bugs
What went wrong:

When attempting to generate 3 unique digits, I called the random module directly.
I received "TypeError: 'module' object is not callable"
To fix this, I used random.sample() function to generate unique numbers for the game.

When I wanted to use a list of strings, I was still using the input I got from the user. I expected a list of strings but instead I got a string.
user_input = input("Enter your guess: ")
list_user_input = list(user_input)
valid_user_code = validate_user_code_guess(user_input, difficulty_level)

Was trying to compare two interger types when thet were an integer and a string. The string was an input from the user and wasn't converted to an integer type. Fixed the issue by using the int() function to then convert the value to an integer type.

I had an issue with validating the game difficulty. The issue was when the game requests to input difficulty, if the user inputs a word or a letter, it should print out (...invalid game difficulty). However, there is a ValueError instead. The program is looking for an integer number of 2, 3 or 4. I updated it so that the program will accept 2, 3 or 4 as a string if the user enters either of this number. After implementing the new code. The game works.

## Validator Testing

[PEP8CI](https://pep8ci.herokuapp.com/) was used to check if there were any errors. Below is the result.

![](/assets/pep8-result.jpg)

- I received an error at line 156 of my code stating "E501 line too long"
- I was unable to remove this error due to it being part of me else statement for validating the users input.

![](/assets/pep8-result-main.jpg)

- In line 181 states ("W292 no newline at end of file")
- I removed this error by placing a new line at the end of the file.

![](/assets/code-testing-result.jpg)
- Above is the result of my last PEP8CI test for code. I am unable to remove the error of line 156 due to id being a necessary code that I cannot change.

**[Back to Table of Contents](#table-of-contents)**

# Deployment 

The game was deployed on Heroku. The following steps were used to deploy the game to Heroku:

  - Sign into Heroku.
  - On the main dashboard choose to Create new app.
  - Choose a unique name for your project and the region, based on where you are located (as I'm in Europe, I chose Europe), and then click on "Create app".
  - Then go to the Settings tab.
  - In Settings click on Reveal Config Vars and enter the following key: PORT and value: 8000.    
  - Next scroll down to Buildpacks and click Add buildpack, choose Python first, then choose Node.js and then click "Save changes".
  - Repeat the above step and select nodejs and click "Save changes".
  - Next go to the Deploy tab.
  - Under the Deployment method, choose GitHub and then click Connect to GitHub you will be prompted to sign into your GitHub.
  - Then you can search for your GitHub repository, in my case this was "bulls-and-calves" and click connect.
  - To deploy automatically you will need to select Enable Automatic Deploys which will rebuild the app every time you push a change to GitHub.
  - To deploy manually go to the Manual deploy section below and click Deploy Branch. Just remember you will need to do this every time you make a change to your code on Github.
  - Below you will see your app was successfully deployed with a view button below this that will take you to the URL of your deployed app.

**[Back to Table of Contents](#table-of-contents)**

# Credits

- Code Institute for the Python Gitpod template
- Heroku as the platform to deploy my project
- My partner for suggesting this game that we both like to play.
- [Stack Overflow](https://stackoverflow.com/) for checking errors that I received while building this project.
- [W3Schools](https://www.w3schools.com/) for being a secondary platform for me to go over certain types of code while trying to implement my code.


**[Back to Table of Contents](#table-of-contents)**