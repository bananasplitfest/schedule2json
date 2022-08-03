import csv
import os
from os import path
import shutil
import pathlib
import re
import glob
import json

remove_previous_files = True
filename = "2022 GABSC schedule.xlsx - Activities.csv"

output_file = '2022-schedule.json'

title = 0
pre = 1
post = 2
description = 13
start = 3
end = 4
highlight = 23
location = 5
link =6
button1 = 7
button1link = 8
button2 = 9
button2link = 10
imageSchedule = 11
imageScheduleAlt = 12
imagePage = 26
imagePageAlt = 27
genre = 14
website = 15
facebook = 16
instagram = 17
twitter = 18
spotify = 19
appleMusic = 20
youtube = 21
tiktok = 22
entertainer = 24
activity = 25




line = 0
output = "["

with open(filename, 'r') as file:
    csvreader = csv.reader(file)

    fields = next(csvreader)

    for row in csvreader:
        links = row[website] or row[facebook] or row[instagram] or row[twitter] or row[spotify] or row[appleMusic] or row[youtube] or row[twitter]

        new_row = ''
        new_row += "{"
        new_row += "\"title\": \"" + row[title] + "\","
        if row[pre]:
            new_row += "\"pre\": \"" + row[pre] + "\","
        if row[post]:
            new_row += "\"post\": \"" + row[post] + "\","
        if row[start]:
            new_row += "\"start\": \"" + row[start].strip() + "\","
        if row[end]:
            new_row += "\"end\": \"" + row[end].strip() + "\","
        if row[location]:
            new_row += "\"resourceId\": \"" + row[location] + "\","
        if row[link]:
            new_row += "\"link\": \"" + row[link] + "\","
        if row[description]:
            new_row += "\"description\": \"" + row[description] + "\","
        if row[imageSchedule] or row[imagePage]:
            new_row += "\"image\": {"
            temp = ''
            if row[imageSchedule]:
                temp += "\"schedule\": {"
                temp += "\"type\": \"schedule\","
                temp += "\"file\": \"" + row[imageSchedule] + "\","
                temp += "\"alt\": \"" + row[imageScheduleAlt] + "\""
                temp += "},"
            if row[imagePage]:
                temp += "\"page\": {"
                temp += "\"type\": \"page\","
                temp += "\"file\": \"" + row[imagePage] + "\","
                temp += "\"alt\": \"" + row[imagePageAlt] + "\""
                temp += "},"
            temp = temp[:-1] if temp[-1]==',' else temp
            new_row += temp
            new_row += "},"
        if row[button1] or row[button2]:
            temp = ''
            temp += "\"buttons\": ["
            if row[button1]:
                temp += "{"
                temp += "\"title\": \"" + row[button1] + "\","
                temp += "\"link\": \"" + row[button1link] + "\""
                temp += "},"
            if row[button2]:
                temp += "{"
                temp += "\"title\": \"" + row[button2] + "\","
                temp += "\"link\": \"" + row[button2link] + "\""
                temp += "},"
            temp = temp[:-1] if temp[-1]==',' else temp
            temp += "],"
            new_row += temp
        if row[website] or row[facebook] or row[instagram] or row[twitter] or row[spotify] or row[appleMusic] or row[youtube] or row[tiktok]:
            temp = ''
            temp += "\"links\": ["
            if row[website]:
                temp += "{"
                temp += "\"type\": \"website\","
                temp += "\"link\": \"" + row[website] + "\""
                temp += "},"
            if row[facebook]:
                temp += "{"
                temp += "\"type\": \"facebook\","
                temp += "\"link\": \"" + row[facebook] + "\""
                temp += "},"
            if row[instagram]:
                temp += "{"
                temp += "\"type\": \"instagram\","
                temp += "\"link\": \"" + row[instagram] + "\""
                temp += "},"
            if row[twitter]:
                temp += "{"
                temp += "\"type\": \"twitter\","
                temp += "\"link\": \"" + row[twitter] + "\""
                temp += "},"
            if row[spotify]:
                temp += "{"
                temp += "\"type\": \"spotify\","
                temp += "\"link\": \"" + row[spotify] + "\""
                temp += "},"
            if row[appleMusic]:
                temp += "{"
                temp += "\"type\": \"appleMusic\","
                temp += "\"link\": \"" + row[appleMusic] + "\""
                temp += "},"
            if row[youtube]:
                temp += "{"
                temp += "\"type\": \"youtube\","
                temp += "\"link\": \"" + row[youtube] + "\""
                temp += "},"
            if row[tiktok]:
                temp += "{"
                temp += "\"type\": \"tiktok\","
                temp += "\"link\": \"" + row[tiktok] + "\""
                temp += "},"
            temp = temp[:-1] if temp[-1]==',' else temp
            temp += "],"
            new_row += temp
        if row[entertainer]:
            new_row += "\"entertainer\": " + row[entertainer].lower() + ","
        if row[highlight]:
            new_row += "\"highlight\": " + row[highlight].lower() + ","
        if row[activity]:
            new_row += "\"activity\": " + row[activity].lower() + ","
        if row[genre]:
            new_row += "\"genre\": \"" + row[genre] + "\","

        new_row = new_row[:-1] if new_row[-1]==',' else new_row
        new_row += "}"
        new_row += ","
        output += new_row
        line += 1

output = output[:-1] if output[-1]==',' else output
output += "]"

# output = re.sub(r',\s\]', ']', output)

# print(output)

json_object = json.loads(output)

json_formatted_str = json.dumps(json_object, indent=2)

output = json_formatted_str

print(output)

print("Total no. of rows: %d"%(csvreader.line_num))

f = open("./"+output_file, "w")
f.write(output)
f.close()