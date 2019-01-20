import json
from pprint import pprint
import subprocess
import os

regions = ["ashanti","central", "western_north", "western", "eastern", "greater_accra", "oti", "bono", "ahafo", "bono_east", "sunyani", "northern", "volta", "north_east", "upper_east", "upper_west"]

#  mapshaper -i map_outline.json -simplify 1% keep-shapes -o map_outline_edit.geojson
for region in regions:
    cmd = '/cygdrive/c/Users/Daniel/AppData/Roaming/npm/mapshaper -i {2}/{0} -simplify 10% keep-shapes -o {2}/{1}'.format("map_out.json", "map_out_mapshaper.json", region)
    print os.system(cmd)
    print "done with {0}!".format(region)