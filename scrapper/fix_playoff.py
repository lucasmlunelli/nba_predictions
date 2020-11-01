# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 20:49:17 2018

@author: lunel
"""

import os, json

# this finds our json files
path_to_json = 'C:/Users/lunel/Desktop/post/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

for file in json_files:
    with open(path_to_json+file, "r") as jsonFile:
        data = json.load(jsonFile)

    tmp = data["type"]
    data["type"] = "playoffs"
    
    with open(path_to_json+file, "w") as jsonFile:
        json.dump(data, jsonFile)