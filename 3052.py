# inputs & variables
n = 0
mods = set()

# func & classes

# main logic
for _ in range(10):
  mods.add(int(input()) % 42)
print(len(mods))