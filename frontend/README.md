# Typing Game Vue Project

This project contains a "Typing Game" that helps users test their typing speed. Users are presented with random sentences and are expected to type these sentences correctly.

## Project Description

The project has been developed using Vue.js and primarily features the following:

- The user clicks the "Play" button to start the game.
- Randomly selected sentences are displayed, and the user attempts to type these sentences into a text input field.
- The input text is compared with the correct sentence to determine accuracy.
- If the input is correct, a "Correct!" message is displayed; otherwise, a "Wrong!" message is shown.
- When the user types a sentence correctly, the next sentence is presented.
- At the end of the game, the total time taken to complete the game is displayed to the user.
- After completing the game, the user can choose to play again or exit using the "Play Again" or "Exit" options.

## Project Setup

1. Open a terminal in the project's main directory.
2. Run the following command to install the required dependencies:

    ```bash
    npm install
    ```

Use the following command to run the project on a local server:

    ```bash
    npm run serve
    ```

## Notes
The game data is assumed to be fetched from the server, including randomly selected sentences and time intervals. You need to configure the server-side and data structures accordingly.
This project represents a basic example of a "Typing Game" application. Additional features or improvements should be added based on your requirements.

