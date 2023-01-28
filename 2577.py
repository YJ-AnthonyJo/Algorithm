# inputs & variables
A = int(input())
B = int(input())
C = int(input())
s = ''
# func & classes

# main logic
s = str(A*B*C)
for t in range(0,10):
  print(s.count(str(t)))