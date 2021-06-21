from pandas.io.json import json_normalize
import pandas as pd
import requests
import folium
import json
import overpass


url = 'http://overpass-api.de/api/interpreter'  # Overpass API URL
query = """
    [out:json][timeout:25];
    // fetch area “Danmark” to search in
    {{geocodeArea:Danmark}}->.searchArea;
    // gather results
    (
      // query part for: “boundary=administrative”
      relation["boundary"="administrative"](area.searchArea);
    );
    // print results
    out body;
    >;
    out skel qt;
    """
r = requests.get(url, params={'data': query})

#data = json.loads(r.json())
#df = pd.json_normalize(data['results'])


#osmMap = folium.Map(location=[48.85, 2.35], tiles="OpenStreetMap", zoom_start=10)
#osmMap.save('AaA.html')
#osmMap

