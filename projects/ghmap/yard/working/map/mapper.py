import json
from pprint import pprint

regions = ["ashanti","central", "western_north", "western", "eastern", "greater_accra", "oti", "bono", "ahafo", "bono_east", "sunyani", "northern", "volta", "north_east", "upper_east", "upper_west"]

# Read map default skeleton
with open('map_default.json') as fd:
        default_data = json.load(fd)

# Read features of each region
for region in regions:
    with open('{0}/map_out.json'.format(region)) as f:
        data = json.load(f)
    
    # Push into mapper json
    for d in data['features']:
        default_data['features'].append(d)

# Create mapper output file
with open("mapper.json", 'w') as fh:
        json.dump(default_data, fh)