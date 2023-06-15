# File containing the methods to perform calculations

def val_average(arr):
    total = 0
    count = 0

    for item in arr:
        total += item
        count += 1

    return total / count

