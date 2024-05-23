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

        try:
            image_data = requests.get(url).content 
        
            # Opening a new file named img with extension .jpg 
            # This file would store the data of the image file 
            image_f = open(filepath, 'wb') 
            
            # Storing the image data inside the data variable to the file 
            image_f.write(image_data)
        except Exception as e:
            print(e)
            print(url)
            print()
            
            # Create file
            open(filepath, 'a').close()


f.close()