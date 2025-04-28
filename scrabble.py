letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# 1. Build the point dictionary:

# Creates a dictionary using dictionary comprehension that has the elements of 'letters' as the keys and the elements of 'points' as the values
letter_to_points = {key:value for key, value in zip(letters, points)}

# Adds a blank tile to the dictionary
letter_to_points[' '] = 0

# 2. Score a word:

# A function that takes in a word and returns how many points the word is worth
def score_word(word):
	point_total = 0
	for letter in word:
		point_total += letter_to_points.get(letter, 0)
	return point_total

# 3. Score a game:

# Dictionary that maps players to a list of the words they have played
player_to_words = {
"player1": ["BLUE", "TENNIS", "EXIT"],
"wordNerd": ["EARTH", "EYES", "MACHINE"],
"Lexi Con": ["ERASER", "BELLY", "HUSKY"],
"Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

# Dictionary that maps players to the total points for the words they have played
player_to_points = {}

# A function that loops through the player_to_words dictionary to calculate the total score for each player and adds them to the player_to_points dictionary
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points

# A function that takes in a player and a word, and adds that word to the list of words they've played in the player_to_words dictionary
def play_word(player, word):
	if player in player_to_words:
		player_to_words[player].append(word.upper()) 
	else:
		player_to_words[player] = [word.upper()]
	update_point_totals()
    
update_point_totals()

print(player_to_words)
print("")
print(player_to_points)

# Alternatives:
# We can also use the code below when instantiating the letter_points_dictionary to handle lowercase within the dictionary instead of using upper() in the play_word() function. Although the duplication of keys is involved with this option, it allows for maximum speed at runtime, without the upper() function calls later on.

# If we need to keep the memory small, with no duplicate letter entries, then using upper() within the play_word() function is the best option as it will convert the letters at runtime.

# letter_to_points = {}
# for letter, point in zip(letters, points):
#     letter_to_points[letter] = point
#     letter_to_points[letter.lower()] = point