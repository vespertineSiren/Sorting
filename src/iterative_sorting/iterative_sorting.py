# TO-DO: Complete the selection_sort() function below 

def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        smallest_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap_flag = True
    while swap_flag:
        swap_flag = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap_flag = True
    return arr




# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr