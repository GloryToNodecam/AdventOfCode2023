import re
numberD = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


with open("Day1Part1Data.txt") as f:
    total = 0
    text = f.readlines()
    for line in text:
        for key in numberD.keys():
            line = line.replace(key, key[0] + str(numberD[key]) + key)
        tempNumber = re.findall(r"\d", line)
        if len(tempNumber)  == 1:
            total += int(tempNumber[0]) * 11
        else:
            total += (int(tempNumber[0]) * 10) + int(tempNumber[-1])
    print(total)
    
    