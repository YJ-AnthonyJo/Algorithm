# inputs & variables
h, m = map(int, input().split())

# func & classes

# main logic
m -= 45
if m < 0:
  h -= 1
  m += 60
if h < 0:
  h += 24
print(h, m)