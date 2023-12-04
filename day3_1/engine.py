import pandas as pd
import re

def value_at(i):
    if (i >= 0 and i < dataframe.count()['value']):
        return dataframe.at[i, 'value']
    
def contains_symbol(string):
    return string != None and re.search(symbol_regex, string)

def excerpt(string, start, end):
    if string != None:
        return string[start:end]
    else:
        return None

symbol_regex = r'[^\d.]'
number_regex = r'\d+'

dataframe = pd.read_csv('input', names=['value'])
result = 0

for i, row in dataframe.iterrows():
    last_line = value_at(i-1)
    this_line = row['value']
    next_line = value_at(i+1)

    for m in re.finditer(number_regex, this_line):
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

        if contains_symbol(last_line_excerpt) or contains_symbol(this_line_excerpt) or contains_symbol(next_line_excerpt):
            result += int(m.group())

print(result)