# QUIZ

This quiz is a simple game played on the command line. This is a quiz with multiple choice general knowledge questions.
Users can try to guess the answer by inputting letter as an answer.

You can view the live site here - [QUIZZ](https://quizz-quest.herokuapp.com/).

![The quiz preview at different resolutions](assets/docs/amiresponsive_screen.png "The quiz preview")

## Contents

+ [User Experience](#user-experience)
  + [User Stories](#user-stories)
  + [Flowchart](#flowchart)
  + [Design](#design)
+ [Features](#features)
  + [Start](#start)
  + [Playing The Game](#playing-the-game)
  + [Quiz Results](#quiz-results)
  + [End of Game](#end-of-game)
+ [Tecnologies Used](#technologies-used)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## User Experience

### User Stories

+ As a user I want to understand how the game works.
+ As a user I want to have fun and test my knowledge
+ As a user I want to know the result of the game
+ As a user I want to be able to restart the game

[Back to top](#contents)

### How to play

The quiz is made similar to those that can often be found on the Internet.
The quiz is made by analogy with those that can often be found on the Internet.
Game logic should be intuitive to the user.

+ The program presents one by one general knowledges questions and multiple answers below question

+ The player then chooses and input letter that he/she thinks will be apropriate for an aswer

+ After cycling through all questions the program presents results of game displaing correct answers and user answers in appropriate named rows

+ Then the game offers to player play again and otherwise return to the start screen.

[Back to top](#contents)

### Flowchart

As this game is played in the console I did a simple flowchart to get a map for that how I wanted it to work.

![Flowchart](assets/docs/quiz_flowchart.png)

### Design

As the quiz takes place through the terminal, I've highlighted the messages in color for the user to better understand the progress of the game and the results of the quiz.

[Back to top](#contents)

## Features

### Start

When the quiz starts, the user sees a start screen with logo and prompts for enter a name

![Start screen](assets/docs/start_screen.png)

### Playing the quiz

+ When playing the quiz you receive message in green when the guess is correct.
+ If you guess wrong you receive message in red color

![In play](assets/docs/quiz_flow.png)

### Quiz Results

When the quiz is finished the quiz results will be presented to the user so that he can compare the correct answers and his own answers. The result of the quiz will also be shown in percentage and quantitative terms.

![Quiz results](assets/docs/quiz_results.png)

### End of quiz

+ User can choose if he/she wants to play again or return to main screen.

![Quiz finish](assets/docs/quiz_finish.png)

+ If user choose quit quiz the thank message displayed for user and quiz returns start screen.

![End of game](assets/docs/quiz_thank_message.png)

[Back to top](#contents)


## Technologies Used

+ [Figma](https://www.figma.com/) was used to create the flowchart
+ [Gitpod](https://www.gitpod.io/) was used to create all files with code
+ [Python](https://www.python.org/)
+ [GitHub](https://github.com/) was used for storing the code repository
+ [Heroku](https://heroku.com/) was used to deploy the program live version
+ [Am I Responsive](http://ami.responsivedesign.is/) to generate an image showcasing the game responsivness to different screen sizes

[Back to top](#contents)