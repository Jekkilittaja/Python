import pandas as pd

data = pd.read_csv('chip_dataset.csv', sep= '\t', encoding='utf-8')
print(data.columns)