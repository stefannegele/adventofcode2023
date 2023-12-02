import pandas as pd

dataframe = pd.read_csv('input', names=['name', 'values'], sep=":")

dataframe['values'] = dataframe['values'].str.split(';')\
    .transform(lambda l: [i.split(',') for i in l])\
    .transform(lambda l: [i for sl in l for i in sl])\
    .transform(lambda l: [i.strip().split(' ') for i in l])\
    .transform(lambda l: [[int(i[0]), i[1].strip()] for i in l])\
    .transform(lambda l: pd.DataFrame(l, columns=['count', 'color']).groupby('color').max().apply(lambda g: g['red'] * g['green'] * g['blue']))

print(dataframe['values'].sum())
