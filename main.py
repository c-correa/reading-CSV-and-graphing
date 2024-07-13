import csv

data_list = []

with open("./programming_language.csv", "r", newline='') as csvfile:
    dic = csv.reader(csvfile, delimiter=",")
    header = next(dic)
    for row in dic:
        iterable = {header[i]: row[i] for i in range(len(header))}
        data_list.append(iterable)
print(data_list)
