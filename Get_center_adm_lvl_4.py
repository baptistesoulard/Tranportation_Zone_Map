import json
import pandas as pd

with open('superheroes.json') as f:
    superHeroSquad = json.load(f)
print(type(superHeroSquad))
# Output: dict
print(superHeroSquad.keys())
# Output: dict_keys(['squadName', 'homeTown', 'formed', 'secretBase', 'active', 'members'])

df = pd.read_json('superheroes.json')
print(df.head())