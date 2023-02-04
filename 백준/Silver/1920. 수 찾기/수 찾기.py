

# input & global variables
n = int(input())
A = list(map(int,input().split()))
Mn = int(input())
M = list(map(int,input().split()))



#func
def find(t):
  l = 0
  r = n - 1
  while l <= r:
    mid = (l+r) // 2
    if A[mid] == t:
      return True 
    if A[mid ] >= t:
      r = mid - 1
    else:
      l = mid + 1
  return False

#main logic
A.sort()
for e in M:
  if find(e):
    print('1')
  else:
    print('0')