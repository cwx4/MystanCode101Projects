"""
File: anagram.py
Name: Sylvia Chang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import timeit

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

dic_lst = []
permutation_lst = []


def main():
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    read_dictionary()
    while True:
        word = str(input('Find Anagrams for:'))
        if word == EXIT:
            # return "-".join(str(n) for n in range(100))
            break
        else:
            find_anagrams(word)


def read_dictionary():
    global dic_lst
    with open(FILE, 'r') as f:
        for line in f:
            dic_lst.append(line.strip())


def find_anagrams(s):
    """
    :param s: str, a word to be permuted
    :return: lst, any permutation of s in dic_lst
    """
    global permutation_lst

    helper(s, [])
    print(f'{len(permutation_lst)} anagrams:{permutation_lst}')
    permutation_lst = []


def helper(s, current_s):
    global dic_lst, permutation_lst

    permutation_s = ''
    for k in current_s:
        permutation_s += s[k]

    if has_prefix(permutation_s):
        if len(current_s) == len(s):
            if permutation_s in dic_lst and permutation_s not in permutation_lst:
                permutation_lst.append(permutation_s)
                print(f'Found: {permutation_s}')
                print('Searching...')
        else:
            for j in range(len(s)):
                if j not in current_s:
                    # Choose
                    current_s.append(j)
                    # Explore
                    helper(s, current_s)
                    # Un-choose
                    current_s.pop()


def has_prefix(sub_s):
    """
    :param sub_s: str
    :return: bool, if the sub_s in dic_lst
    """
    for word in dic_lst:
        if word.startswith(sub_s):
            return True
    return False


# def helper(s, current_s):
#     global dic_lst, permutation_lst
#
#     if has_prefix(s, current_s):
#         if len(current_s) == len(s):
#             permutation_s = ''
#             for i in current_s:
#                 permutation_s += s[i]
#             if permutation_s in dic_lst and permutation_s not in permutation_lst:
#                 permutation_lst.append(permutation_s)
#                 print(f'Found: {permutation_s}')
#                 print('Searching...')
#         else:
#             for j in range(len(s)):
#                 if j not in current_s:
#                     # Choose
#                     current_s.append(j)
#                     # Explore
#                     helper(s, current_s)
#                     # Un-choose
#                     current_s.pop()
#
#
# def has_prefix(s, current_s):
#     """
#     :param s:
#     :param current_s:
#     :return:
#     """
#     sub_s = ''
#     for k in current_s:
#         sub_s += s[k]
#     for word in dic_lst:
#         if word.startswith(sub_s):
#             return True
#     return False


t = timeit.timeit(main(), number=10000)
print('執行時間：%f 秒' % t)


if __name__ == '__main__':
    main()
