# inputs & variables
numbers = list(map(int, input().split()))

# func & classes

# main logic
if numbers == sorted(numbers):
  print('ascending')
elif numbers == sorted(numbers, reverse=True):
  print('descending')
else:
  print('mixed')