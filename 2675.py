# inputs & variables
n1, n2 = map(int, input().split())
N1, N2 = 0, 0
# func & classes

# main logic
while n1 // 10:
  N1 += n1 % 10
  N1 *= 10
  n1 //= 10
N1 += n1 % 10

while n2 // 10:
  N2 += n2 % 10
  N2 *= 10
  n2 //= 10
N2 += n2 % 10

print(N1 > N2 and N1 or N2)