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

  # TO-DO: add missing code
  while len(arr) > 0:
    middle = int(len(arr) / 2)
    middle_test = arr[middle]
    if middle_test == target:
      return target
    elif middle_test > target:
      arr = arr[:middle]
    else:
      arr = arr[middle + 1:]

  return -1  # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target):
  # middle = (low + high) // 2
  if len(arr) == 0:
    return -1  # array empty

  # TO-DO: add missing if/else statements, recursive calls
  while len(arr) > 1:
    middle = int(len(arr) / 2)
    if arr[middle] == target:
      arr = arr[middle:middle + 1]
    elif arr[middle] > target:
      arr = binary_search_recursive(arr[:middle], target)
    else:
      arr = binary_search_recursive(arr[middle + 1:], target)
  return arr