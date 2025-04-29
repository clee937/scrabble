# Scrabble

## About

Scrabble is a program that uses dictionaries to organise players, words, and points to process the data for a group of friends playing scrabble.

## Features and code breakdown

### Dictionaries:

- `letter_to_points`: contains key value pairs of all the letters and the number of points they are worth.
- `player_to_words`: maps players to a list of the words they have played.
- `player_to_points`: maps players to the total points for the words they have played.

### Functions:

- `score_word()`: takes a word as a parameter and uses a **for loop** to iterate through each letter and retrieve the points for each letter from the `letter_to_points` dictionary. The function returns the total number of points the word is worth.
- `update_point_totals()`: iterates through the `player_to_words` dictionary with a nested loop to calculate the total score for each player and adds them to the `player_to_points` dictionary.
- `play_word()`: takes in a player and their word as parameters, and adds the word to the list of words played in the `player_to_words` dictionary. Calls `update_point_totals()` to update the points in the `player_to_points` dictionary.

## Technologies used

- Python
