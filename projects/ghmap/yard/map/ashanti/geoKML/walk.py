import json
from pprint import pprint

with open('map.json') as f:
    data = json.load(f)

for d in range(len(data['features'])):
    data['features'][d]['properties']['name'] = "dummy_object_{1}".format(d)
    data['features'][d]['id'] = "dummy_id_{0}".format(d)
# pprint(data)

with open("map_out.json", 'w') as f:
    json.dump(data, f)