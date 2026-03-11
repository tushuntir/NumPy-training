import pandas as pd

data = pd.read_csv('data.csv')

pd.options.display.max_rows=999
x = data["Calories"].mode()[0]
data.fillna({"Calories": x}, inplace=True)
save= data.to_csv('data.csv')

print(data)