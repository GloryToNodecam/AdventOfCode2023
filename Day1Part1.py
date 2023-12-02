import re

with open("Day1Part1Data.txt") as f:
    total = 0
    text = f.readlines()
    for line in text:
        tempNumber = re.findall(r"\d", line)
        if len(tempNumber)  == 1:
            total += int(tempNumber[0]) * 11
        else:
            total += (int(tempNumber[0]) * 10) + int(tempNumber[-1])
    print(total)