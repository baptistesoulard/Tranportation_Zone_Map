import requests
import json
import csv
import pandas as pd

overpass_url = 'http://overpass-api.de/api/interpreter'
overpass_query = '''
    [out:csv(name,capital,::lat,::lon;true;";")][timeout:250];
    {{geocodeArea:Portugal}}->.searchArea;
    
    (
      node["capital"="yes"](area.searchArea);
      node["capital"="4"](area.searchArea);
    );
    
    out body;
    >;
    out skel qt;
    '''


response = requests.get(overpass_url, params={'data': overpass_query})

data = response.content

print(response.text)
