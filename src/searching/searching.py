# STRETCH: implement Linear Search				
def linear_search(arr, target):
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i
  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1  # array empty

  min = 0
  max = len(arr) - 1

  # TO-DO: add missing code
  while min <= max:
    middle = int((min + max) / 2)
    middle_test = arr[middle]
    if middle_test < target:
      min =  middle + 1
    elif middle_test > target:
      max = middle - 1
    else:
      return middle

  return -1  # not found



# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  middle = (low + high) // 2

  if len(arr) == 0:
    return -1  # array empty
  # TO-DO: add missing if/else statements, recursive calls


