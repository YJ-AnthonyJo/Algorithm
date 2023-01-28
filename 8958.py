# inputs & variables
N = int(input())
s = ''
score = 1
total = 0
# func & classes

# main logic
for _ in range(N):
  total = 0
  score = 1
  s = input()
  for c in s:
    if c == 'X':
      score = 1
    if c == 'O':
      total += score
      score += 1
  print(total)
  