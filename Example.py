import json
import pandas as pd


def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct



with open('data-json-test2.json') as json_file:
    data = json.load(json_file)

print(data.keys())


df = pd.DataFrame(data['elements'])
print(df.head())
coordinates = df['center'].apply(pd.Series)
print(type(coordinates))
name = df['tags'].apply(pd.Series)['name:en'].to_frame()
print(type(name))

province_center = pd.concat([name, coordinates], axis=1, join="inner")
print(province_center)

#df.to_csv('df2.csv')