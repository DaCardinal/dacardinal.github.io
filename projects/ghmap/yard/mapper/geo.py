import os
import errno
import requests
import re
import json
import fileinput

# set arguments
fileformat = ''
filefolder = ''
converttype = 'kml'
regions = ["ashanti", "western_north", "western", "eastern", "greater_accra", "oti", "bono", "ahafo", "bono_east", "sunyani", "northern", "volta", "north_east", "upper_west", "central", "upper_east"]
for region in regions:
    # svg file to convert
    filetoconvert = "{0}/{0}.svg".format(region)
    # filetoconvert = "{0}/geodata/{0}.geojson".format(region)

    if converttype == 'geojson':
        # svg to json
        fileformat = 'geojson'
        filefolder = 'geodata'

    if converttype == 'kml':
    # svg to kml
        fileformat = 'kml'
        filefolder = 'geoKML'

    # output filename
    filename = "{0}/{1}/{0}.{2}".format(region, filefolder, fileformat)

    # convert svg to kml/geojsons
    url = 'https://mygeodata.cloud/api/convert'
    # url = 'https://mygeodata.cloud/api/datasetinfo'
    data = {'format': fileformat, 'outcrs': 'EPSG:4326', 'outform': 'binary', 'key': 'EwnCSYhSpMH39ma'}
    files = {'file': open(filetoconvert, 'rb')}
    r = requests.post(url, files=files, data=data)

    # create file name if doesn't exist
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    # write to output file, replace linestring in kml to linear rings
    with open(filename, 'w') as f:
        for chunk in r.iter_content(1000):
            
            # replace if kml
            if fileformat is 'kml':
                chunk = chunk.replace("<LineString>", "<Polygon><outerBoundaryIs><LinearRing>")
                chunk = chunk.replace("</LineString>", "</LinearRing></outerBoundaryIs></Polygon>")
            f.write(chunk)
    print "{0} region done!".format(region)

