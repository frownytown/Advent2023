inputfile = r'C:\Users\roger\CodeProjects\Advent2023\Day1\input.txt'

with open(inputfile, 'r') as input:
    overall = []
    sumlist = []
    for line in input:
        lines_digits = []
        for char in line:
            if char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                lines_digits.append(char)
        overall.append(lines_digits)
    for entry in overall:
        valueone, valuetwo = entry[0], entry[-1]
        hold = valueone + valuetwo
        sumlist.append(int(hold))
    print(sum(sumlist))

