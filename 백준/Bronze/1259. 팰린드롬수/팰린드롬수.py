# input & global variables
N = input()

#func

#main logic
while N != '0':
  R = list(N)
  R.reverse()
  R = ''.join(R)
  if R == N:
    print("yes")
  else:
    print("no")
  N = input()