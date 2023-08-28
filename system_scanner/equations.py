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


# This is probably overly-complex, dont think its needed and can just use the equation in the method below
def is_over(x, y):
    if x > y:
        return True
    else:
        return False


def percentage_dif(x, y):
    results = is_over(x, y)
    if results is True:
        ans = (x - y)
    else:
        ans = (y - x)

    return ans


def find_ram_as_percentage(total, available):
    return (total - available) / total * 100
