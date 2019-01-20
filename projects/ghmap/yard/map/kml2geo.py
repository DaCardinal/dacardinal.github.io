import os, errno
import requests, re, json, fileinput

count = 199
# regions = ["ashanti", "western_north", "oti", "bono", "western", "eastern", "greater_accra", "ahafo", "bono_east", "sunyani", "northern",
#  "volta", "north_east", upper_east, upper_west]
# "central"
regions  = ["central"]

for region in regions:
    fileformat = 'geojson'
    filetoconvert = "{0}/geoKML/{0}.kml".format(region)

    url = 'https://mygeodata.cloud/api/convert'
    data = {'format': fileformat, 'outcrs': 'EPSG:4326', 'outform': 'binary', 'key': 'EwnCSYhSpMH39ma'}
    files = {'file': open(filetoconvert, 'rb')}
    r = requests.post(url, files=files, data=data)
    
    filename = "{0}/map.json".format(region)
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(filename, 'w') as fd:
        for chunk in r.iter_content(1000):
            fd.write(chunk)
    print "{0} region done converting to geojson!".format(region)

    # load json
    with open(filename) as f:
        data = json.load(f)

    # clean up properties tag
    for d in range(len(data['features'])):
        count += 1
        data['features'][d]['properties']['name'] = "dummy_object_{0}".format(count)
        data['features'][d]['id'] = "dummy_id_{0}".format(count)
        
    print count
    with open("{0}/map_out.json".format(region), 'w') as f:
        json.dump(data, f)

