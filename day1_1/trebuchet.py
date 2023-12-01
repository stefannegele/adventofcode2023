import pandas as pd

dataframe = pd.read_csv('input', names=['values'])
series = dataframe['values'].squeeze()
strings = series.str.findall(r'(\d)')
digits = strings.transform(lambda d: int(d[0] + d[len(d)-1]))
result = digits.sum()

print(result)