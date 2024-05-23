import json
import requests
import os

f = open('controlled_noisy_web_labels/dummy_data/dataset_no_images/mini-imagenet-annotations.json')
data = json.load(f)

path = "controlled_noisy_web_labels/dummy_data/dataset_no_images/noisy_images/"

for j in data["data"]:
    for i in j:
        url = i["image/uri"]
        filename = i["image/id"]

        filepath = path + filename + ".jpg"

        open(filepath, 'a').close()


f.close()