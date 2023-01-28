# # global variables & inputs
# s = input()
# n_word = 1
# # class & functions

# # main logic
# if s[0] == ' ': s=s[1:]
# if s[-1] == ' ': s=s[:-1]
# while len(s) > 0:
#   i = s.index(' ')
#   if (i + 1 < len(s)) and \
#     (
#       ord('A') <= ord(s[i+1]) <= ord('Z')
#       or
#       ord('a') <= ord(s[i+1]) <= ord('z')
#     ):
#     n_word += 1
#   s = s[i+1:]

# print(n_word) 
# global variables & inputs
s = input()
n_word = 1
# class & functions

# main logic
if s == ' ':
    n_word = 0
    s = ''
if n_word:
    if s[0] == ' ': s=s[1:]
    if s[-1] == ' ': s=s[:-1]

print(s.count(' ') + n_word)