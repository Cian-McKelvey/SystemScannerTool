# In most situations, the use of these algorithms would be needless. However, In the event that there are a lot of
# entries in the list, it could become useful.

# e.g. User scans for 1 minute at 2 checks a second etc...

def bubblesort(arr):
    swapped = False
    # Looping from size of array from last index[-1] to index [0]
    for n in range(len(arr)-1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i + 1]:
                swapped = True
                # swapping data if the element is less than next element in the array
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if not swapped:
            # exiting the function if we didn't make a single swap
            # meaning that the array is already sorted.
            return
            

# Binary search algorithm that returns item index or -1 if item is not present
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target value not found in the array


def find_lowest_value(example_list):
    lowest_value = min(example_list)
    return lowest_value


def find_highest_value(example_list):
    highest_value = 0
    for item in example_list:
        if item > highest_value:
            highest_value = item

    return highest_value
