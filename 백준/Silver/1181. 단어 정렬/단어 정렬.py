# input & global variables
N = int(input())
s = ''
l = set()
#func

#main logic
for _ in range(N):
  s = input()
  l.add(s)

l=sorted(list(l),key=lambda x: (len(x), x))
print(*l, sep='\n') 