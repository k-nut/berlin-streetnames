import json
import requests

def main():
    with open('../data/original.geojson') as infile:
        data = json.load(infile)

    cache = {}    
    for street in data['features']:
        note = street["properties"]["note:de"]
        
        name = note.split('(')[0].strip()
        gender = 'unknown'
        if name not in cache.keys():
            wikidata_id = get_id(name)
            if wikidata_id:
                sex = get_sex(wikidata_id)
                cache[name] = {'sex': sex, 'wikidata_id':wikidata_id}
                print name, wikidata_id, sex
                gender = sex
        else:
            gender = cache[name]['sex']
            print 'using cached ', name
        street["properties"]['gender'] = gender
    with open('../data/with_gender.geojson', 'w') as outfile:
        json.dump(data, outfile)
    
    
def get_id(name):
    base = "https://www.wikidata.org/w/api.php"
    params = {"action": "wbsearchentities",
              "format": "json",
              "language": "en",
              "search": name}
    response = requests.get(base, params=params)
    try:
        match = response.json()["search"][0]['id']
    except IndexError:
        # no matches found
        return None
    return match

def get_sex(wikidata_id):
    base = 'https://www.wikidata.org/w/api.php'
    params = {"action": "wbgetentities",
              "ids": wikidata_id,
              "format": "json",
              "props": "claims"
              }
    response = requests.get(base, params=params)
    sex = response.json()['entities'][wikidata_id]["claims"]["P21"][0]['mainsnak']['datavalue']['value']['numeric-id']
    mapping = {6581097: "male"}
    return mapping[sex]
    
main()
