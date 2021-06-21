import requests

overpass_url = 'http://overpass-api.de/api/interpreter'
overpass_query = '''
    rel["ISO3166-2"~"^FR"]
       [admin_level=4]
       [type=boundary]
       [boundary=administrative];
    out geom;
    '''

response = requests.get(overpass_url, params={'data': overpass_query})
#response.json()

#interesting tags :
# <tag k="name:en" v="Hauts-de-France"/>