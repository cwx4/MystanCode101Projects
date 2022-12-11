"""
File: largest_digit.py
Name: Sylvia Chang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int
	:return: int, biggest digit in integer
	"""
	max_n = 0
	count_lst = [0]
	n = abs(n)
	return helper(n, max_n, count_lst)


def helper(n, max_n, count_lst):
	count_lst[0] += 1
	n_digit = n % 10
	if n_digit > max_n:
		max_n = n_digit
	if n < 10:
		# print(count_lst)
		return max_n
	else:
		n = (n-n_digit)//10
		return helper(n, max_n,  count_lst)


if __name__ == '__main__':
	main()
