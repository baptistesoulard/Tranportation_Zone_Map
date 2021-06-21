import requests
import json
import pandas as pd

overpass_url = 'http://overpass-api.de/api/interpreter'
overpass_query = '''
    [out:json];
    rel["ISO3166-2"~"^GB"]
       [admin_level=5]
       [type=boundary]
       [boundary=administrative];
    out center;
    '''

response = requests.get(overpass_url, params={'data': overpass_query})

data = json.loads(response.content)


with open('data-json-test2.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)


df = pd.DataFrame(data['elements'])
print(df.head())
coordinates = df['center'].apply(pd.Series)
print(type(coordinates))
name = df['tags'].apply(pd.Series)['name'].to_frame()
print(type(name))
province_center = pd.concat([name, coordinates], axis=1, join="inner")
print(province_center)
province_center.to_csv('province_center.csv')

