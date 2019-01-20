import json
from pprint import pprint
import subprocess
import os, requests

regions = ["ashanti","central", "western_north", "western", "eastern", "greater_accra", "oti", "bono", "ahafo", "bono_east", "sunyani", "northern", "volta", "north_east", "upper_east", "upper_west"]



# Get all region info
my_dict = {}
with open("regions.csv", mode='r') as input_file:
    for row in input_file:
        keys = row.rstrip('\n').split(",")
        my_dict[keys[0]] = keys[1].rstrip("\n\r")

# pprint(my_dict)

for region in regions:
    filename = "{0}/map_out_mapshaper.json".format(region)
    fileoutput = "{0}/map_out_named.json".format(region)

    # load json
    with open(filename, 'r') as f:
        filedata = f.read()

    # replace
    for k,v in my_dict.iteritems():
        filedata = filedata.replace("dummy_object_{0}\"".format(k),"{0}\"".format(v))
        filedata = filedata.replace("dummy_id_{0}\"".format(k),"{0}\"".format(v))

    with open(fileoutput, 'w') as f:
        f.write(filedata)
    print "{0} region done!".format(region)