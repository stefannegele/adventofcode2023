import pandas as pd

max_red = 12
max_green = 13
max_blue = 14

dataframe = pd.read_csv('input', names=['name', 'values'], sep=":")

dataframe['name'] = dataframe['name'].str.removeprefix('Game ').transform(lambda s: int(s))

dataframe['values'] = dataframe['values'].str.split(';')\
    .transform(lambda l: [i.split(',') for i in l])\
    .transform(lambda l: [i for sl in l for i in sl])\
    .transform(lambda l: [i.strip().split(' ') for i in l])\
    .transform(lambda l: [[int(i[0]), i[1].strip()] for i in l])\
    .transform(lambda l: any(i[0] > max_red and i[1] == 'red' for i in l) or any(i[0] > max_green and i[1] == 'green' for i in l) or any(i[0] > max_blue and i[1] == 'blue' for i in l))

dataframe = dataframe.query('values == False')

print(dataframe['name'].sum())
