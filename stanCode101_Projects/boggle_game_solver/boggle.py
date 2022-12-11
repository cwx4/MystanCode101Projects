"""
f y c l
i o m g
o r i l
h j h u
"""


"""
File: boggle.py
Name: Sylvia Chang
----------------------------------------
This program presents the word game Boggle.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
COL = 4
ROW = 4

dic_lst = []
found_lst = []


def main():
	"""
	User input the letter in legal format , and the program start to search word exist in dictionary
	"""

	letter_dic = {}
	count = 0

	read_dictionary()

	for i in range(ROW):
		input_s = input(f'{chr(128073)} {i+1} row of letters: ')
		input_lst = input_s.split()
		if len(input_lst) != ROW:
			print(f'Illegal input{chr(128581)}')
			break
		else:
			for k in range(len(input_lst)):
				if len(input_lst[k]) != 1:
					print('Illegal input')
					break
				else:
					for j in range(COL):
						position, letter = (i, j), input_lst[j]
						letter_dic[position] = letter
		count += 1
	# if every row is input in legal format, start search word in dictionary
	if count == ROW:
		# print(letter_dic)
		for key, value in letter_dic.items():
			helper(letter_dic, [], [], [key])

		print(f'There are {len(found_lst)} words in total.{chr(10004)}')


def helper(letter_dic, key_lst, value_lst, start_point_lst):
	f"""
	:param letter_dic: dict, key = position in boggle board, value = letter 
	:param key_lst: lst, all key to search
	:param value_lst: lst, all value to search
	:param start_point_lst: lst, fix the letter for next run of searching
	:return: str, word found
	"""
	global dic_lst, found_lst

	# The coordinate to check letter
	direction = [(0, 0), (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

	permutation_s = ''
	for letter in value_lst:
		permutation_s += letter

	if has_prefix(permutation_s):

		if len(permutation_s) >= 4:
			if permutation_s in dic_lst and permutation_s not in found_lst:
				found_lst.append(permutation_s)
				print(f'{chr(9935)} Found: {permutation_s} {chr(129321)}')
				# find second word
				for j in range(len(direction)):
					position_x, position_y = start_point_lst[-1][0], start_point_lst[-1][1]
					position_x += direction[j][0]
					position_y += direction[j][1]

					search_position = (position_x, position_y)

					if 0 <= position_x < ROW and 0 <= position_y < COL:
						if search_position not in key_lst:
							# Choose
							start_point_lst.append(search_position)
							key_lst.append(search_position)
							value_lst.append(letter_dic[search_position])
							# Explore
							helper(letter_dic, key_lst, value_lst, start_point_lst)
							# Un-choose
							key_lst.pop()
							value_lst.pop()
							start_point_lst.pop()

		else:
			for j in range(len(direction)):
				# fix start letter
				position_x, position_y = start_point_lst[-1][0], start_point_lst[-1][1]
				# Check all direction letter
				position_x += direction[j][0]
				position_y += direction[j][1]

				search_position = (position_x, position_y)

				if 0 <= position_x < ROW and 0 <= position_y < COL:  # letter exist
					if search_position not in key_lst:  # every letter only appear once
						# Choose
						start_point_lst.append(search_position)
						key_lst.append(search_position)
						value_lst.append(letter_dic[search_position])
						# Explore
						helper(letter_dic, key_lst, value_lst, start_point_lst)
						# Un-choose
						key_lst.pop()
						value_lst.pop()
						start_point_lst.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dic_lst
	with open(FILE, 'r') as f:
		for line in f:
			dic_lst.append(line.strip())


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dic_lst:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
