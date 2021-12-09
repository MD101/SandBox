#!/usr/bin/env python3
import re
import operator
import csv
error_count = {}
user_entry_count = {}
with open("log.txt", 'r') as f:
    for lines in f:
        line = re.search(r"ticky: (INFO|ERROR) ([\w ]*) .* \(([a-z.]*)\)$", lines).groups()
        if line[0] == 'ERROR':
            error_count[line[1]] = error_count.get(line[1], 0) + 1
            buff = user_entry_count.get(line[2], [0, 0])
            buff[1] = buff[1] +1
            user_entry_count[line[2]] = buff
        if line[0] == 'INFO':
            buff = user_entry_count.get(line[2], [0, 0])
            buff[0] = buff[0] +1
            user_entry_count[line[2]] = buff
for key, value in user_entry_count.items():
    user_entry_count[key] = tuple(value)
sorted_error_count = sorted(error_count.items(), key=operator.itemgetter(1), reverse=True)
sorted_user_entry_count = sorted(user_entry_count.items(), key=operator.itemgetter(0))
print("sorted error count", error_count)
print("sorted_user_entry_count", user_entry_count)
error_columns = ["Error", "Count"]
user_columns = ["Username", "INFO", "ERROR"]
with open("error_message.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(error_columns)
    for data in sorted_error_count:
        writer.writerow(data)
with open("user_statistics.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(user_columns)
    for data in sorted_user_entry_count:
        line = (data[0], data[1][0], data[1][1])
        writer.writerow(line)
