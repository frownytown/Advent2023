import re

inputfile = r'C:\Users\roger\CodeProjects\Advent2023\Day1\input.txt'

conversion_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


with open(inputfile, 'r') as input:
    search_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    overall = []
    for line in input:
        lines_values = {}
        for element in search_values:
            for match in re.finditer(element, line):
                lines_values[match.group(0)] = match.start()
        sorted_dict = {k: v for k, v in sorted(lines_values.items(), key=lambda item: item[1])}
        list_dict = list(sorted_dict.keys())
        vars = list_dict[0] + list_dict[-1]
        for key in conversion_dict.keys():
            vars = vars.replace(key, conversion_dict[key])
        overall.append(int(vars))
    print(sum(overall))
    #print(overall)


