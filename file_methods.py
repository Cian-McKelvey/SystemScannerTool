import csv


def write_to_file(filepath, content):
    with open(filepath, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(content)


def read_from_file(filepath):
    return_list = []
    with(open(filepath, 'r') as f):
        reader = csv.reader(filepath)
        for row in reader:
            return_list.append(row)
    return return_list
