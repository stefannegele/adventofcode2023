import pandas as pd
import re

def value_at(i):
    if (i >= 0 and i < dataframe.count()['value']):
        return dataframe.at[i, 'value']

def excerpt(string, start, end):
    if string != None:
        return string[start:end]
    else:
        return None

def is_digit(char):
    return char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def find_whole_number(line, position):
    result_string = ''

    while (position > 0 and is_digit(line[position - 1])):
        position -= 1

    while (position < len(line) and is_digit(line[position])):
        result_string += line[position]
        position += 1

    return int(result_string)

def find_whole_numbers(line, line_excerpt, excerpt_start):
    result = []
    for n in re.finditer(number_regex, line_excerpt):
        position = excerpt_start + n.span()[0]
        whole_number = find_whole_number(line, position)
        result.append(whole_number)
    return result

asterisk_regex = r'\*'
number_regex = r'\d+'

dataframe = pd.read_csv('input', names=['value'])
result = 0

for i, row in dataframe.iterrows():
    last_line = value_at(i-1)
    this_line = row['value']
    next_line = value_at(i+1)

    for m in re.finditer(asterisk_regex, this_line):
        span = m.span()

        search_from = span[0]-1
        if (search_from < 0):
            search_from = 0

        search_to = span[1]+1
        if (search_to > len(this_line)):
            search_to = len(this_line)

        last_line_excerpt = excerpt(last_line, search_from, search_to)
        this_line_excerpt = excerpt(this_line, search_from, search_to)
        next_line_excerpt = excerpt(next_line, search_from, search_to)

        adjacent_numbers_in_excerpt = len(re.findall(number_regex, last_line_excerpt)) + len(re.findall(number_regex, this_line_excerpt)) + len(re.findall(number_regex, next_line_excerpt))

        if (adjacent_numbers_in_excerpt == 2):
            adjacent_numbers = find_whole_numbers(last_line, last_line_excerpt, search_from) + find_whole_numbers(this_line, this_line_excerpt, search_from) + find_whole_numbers(next_line, next_line_excerpt, search_from) 
            result += adjacent_numbers[0] * adjacent_numbers[1]

print(result)
