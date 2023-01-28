#input & global variables
s = input()
d = dict()

#functions

#main logic
s = s.upper()
for c in s:
  if c not in d:
    d[c] = 1
  else: d[c] += 1

l = list(d.items())
l.sort(key=lambda x: x[1], reverse=True)

if len(l) > 1:
  if l[0][1] == l[1][1]:
    print('?')
  else:
    print(l[0][0])
else: print(l[0][0])