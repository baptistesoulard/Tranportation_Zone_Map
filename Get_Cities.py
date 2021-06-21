import requests, csv
from time import strftime

ccodes = ['BL', 'DM', 'GD', 'GF', 'GP', 'HT', 'KN', 'LC', 'MF', 'MQ', 'VC']
fclass = 'A'
lang = 'fr'
uname = 'REQUEST FROM GEONAMES'

# Columns to keep
fields = ['countryId', 'countryName', 'countryCode', 'geonameId', 'name', 'asciiName',
          'alternateNames', 'fcode', 'fcodeName', 'adminName1', 'adminCode1',
          'adminName2', 'adminCode2', 'adminName3', 'adminCode3', 'adminName4', 'adminCode4',
          'adminName5', 'adminCode5', 'lng', 'lat']
fcode = fields.index('fcode')

# Divisions to keep
divisions = ['ADM1', 'ADM2', 'ADM3', 'ADM4', 'ADM5', 'PCLD', 'PCLF', 'PCLI', 'PCLIX', 'PCLS']

base_url = 'http://api.geonames.org/searchJSON?'


def altnames(names, lang):
    "Given a dict of names, extract preferred names for a given language"
    aname = ''
    for entry in names:
        if 'isPreferredName' in entry.keys() and entry['lang'] == lang:
            aname = entry.get('name')
        else:
            pass
    return aname


places = []
tossed = []

for country in ccodes:
    data_url = f'{base_url}?name=*&country={country}&featureClass={fclass}&lang={lang}&style=full&username={uname}'
    response = requests.get(data_url)
    data = response.json()  # total retrieved and results in list of dicts
    gnames = response.json()['geonames']  # create list of dicts only
    gnames.sort(key=lambda e: (e.get('countryCode', ''), e.get('fcode', ''),
                               e.get('adminCode1', ''), e.get('adminCode2', ''),
                               e.get('adminCode3', ''), e.get('adminCode4', ''),
                               e.get('adminCode5', '')))
    for record in gnames:
        r = []
        for f in fields:
            item = record.get(f, '')
            if f == 'alternateNames' and f != '':
                aname = altnames(item, 'en')
                r.append(aname)
            else:
                r.append(item)
        if r[fcode] in divisions:  # keep certain admin divs, toss others
            places.append(r)
        else:
            tossed.append(r)

filetoday = strftime('%Y_%m_%d')
outfile = 'geonames_fwi_adm_' + filetoday + '.csv'

writefile = open(outfile, 'w', newline='', encoding='utf8')
writer = csv.writer(writefile, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
writer.writerow(fields)  # header row
writer.writerows(places)
writefile.close()

print(len(places), 'records written to file', outfile)
