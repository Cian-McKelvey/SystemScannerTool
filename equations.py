# File containing the methods to perform calculations

def val_average(arr):
    total = 0
    count = 0

    for item in arr:
        total += item
        count += 1

    return total / count


def is_over_max_usage(arr, value):
    for item in arr:
        if item > value:
            return True
    return False


def find_ram_as_percentage(total, available):
    return (total - available) / total * 100
