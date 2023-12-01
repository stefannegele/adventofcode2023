import pandas as pd

def to_digits(series):
    series = series.replace(to_replace='one', value='1')
    series = series.replace(to_replace='two', value='2')
    series = series.replace(to_replace='three', value='3')
    series = series.replace(to_replace='four', value='4')
    series = series.replace(to_replace='five', value='5')
    series = series.replace(to_replace='six', value='6')
    series = series.replace(to_replace='seven', value='7')
    series = series.replace(to_replace='eight', value='8')
    series = series.replace(to_replace='nine', value='9')
    return series

dataframe = pd.read_csv('input', names=['values'])
series = dataframe['values'].squeeze()

strings = series.str.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')


digits = strings.transform(lambda d: to_digits(pd.Series(d)).to_list())
sums = digits.transform(lambda d: int(d[0] + d[len(d)-1]))

print(sums)

result = sums.sum()

print(result)