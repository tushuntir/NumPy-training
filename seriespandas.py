import pandas as pd
import kagglehub
# a = [1, 2, 4]

# myvar = pd.Series(a, index = ['x', 'y', 'z'])

# print(myvar['y'])

# calories = {'Day 1':420, 'Day 2':554, 'Day 3': 390}

# myvar = pd.Series(calories, index = ["Day 1"])
# print(myvar)

# data = {
#     'calories': [444,555,666],
#     'duration': [60,40,45]
# }
# myvar = pd.DataFrame(data)

# df = pd.DataFrame(data, index=['Day 1', 'Day 2', 'Day 3'])

# print(df)

# print(myvar)


pd.options.display.max_rows = 9999
csv = pd.read_csv('uzw.csv')
print(csv.to_string)

