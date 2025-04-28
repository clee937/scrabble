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
		if letter in letter_to_points:
			point_total += letter_to_points[letter]
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
		player_to_words[player].append(word) 
	else:
		player_to_words[player] = [word]
	update_point_totals()
    
update_point_totals()
print(player_to_points)
print("")

play_word('player1', 'ALLIGATOR')
play_word('code_warrior', 'MOSS')
print(player_to_words)
print("")
print(player_to_points)
print("")
play_word('code_warrior', 'CADENCE')


print(player_to_words)
print("")
print(player_to_points)