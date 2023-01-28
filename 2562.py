# inputs & variables
max = n = int(input())
i = 2
max_i = 1
# func & classes

# main logic
while i < 10:
  n = int(input())
  if n > max:
    max = n
    max_i = i
  i += 1

print(max)
print(max_i)