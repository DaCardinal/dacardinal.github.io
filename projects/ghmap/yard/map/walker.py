import json
from pprint import pprint

# regions = ["western", "central", "eastern", "greater_accra", "oti", "bono", "ahafo", "bono_east", "sunyani", "northern", "volta", "north_east", "upper_east", "upper_west"]

regions = ["upper_east"]

for region in regions:
    with open('upper_east/map.json') as f:
        data = json.load(f)

    count = 184
    for d in range(len(data['features'])):
        count += 1
        data['features'][d]['properties']['name'] = "dummy_object_{0}".format(count)
        data['features'][d]['id'] = "dummy_id_{0}".format(count)
        
    print count
    with open("upper_east/map_out.json", 'w') as f:
        json.dump(data, f)