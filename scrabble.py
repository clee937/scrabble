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

brownie_points = score_word("BROWNIE")

print(f'Brownie points: {brownie_points}')

# 3. Score a game:
