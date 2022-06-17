import json
import base64
import time
import os
import requests
import re

print('''
██████╗  █████╗ ██╗     ██╗      ███████╗    ███╗   ███╗██╗███╗   ██╗██╗    
██╔══██╗██╔══██╗██║     ██║      ██╔════╝    ████╗ ████║██║████╗  ██║██║    
██║  ██║███████║██║     ██║█████╗█████╗      ██╔████╔██║██║██╔██╗ ██║██║    
██║  ██║██╔══██║██║     ██║╚════╝██╔══╝      ██║╚██╔╝██║██║██║╚██╗██║██║    
██████╔╝██║  ██║███████╗███████╗ ███████╗    ██║ ╚═╝ ██║██║██║ ╚████║██║    
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══════╝    ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝    
                                                            @zer0mania                 

This AI can generate images based on prompts you give, it can take 1.5-3 minutes to generate and makes 9 256x256 images and saves it.
''')

while True:
    prompt = input("Enter prompt: ")
    print("Generating..")
    while True:
        url = "https://bf.dallemini.ai:443/generate"
        json = {"prompt": f"{prompt}"}
        tic = time.perf_counter()
        response = requests.post(url, json=json)
        if "mega-1:v16" in response.text:
            break
        print(response.text)

    data = response.json()

    count = 1
    dir = re.sub('[^A-Za-z0-9]+_', '', prompt.replace(' ','_')) + "_" + str(int(time.time()))

    os.mkdir(dir)

    for i in data["images"]:
        img_data = i.replace('\n','')
        with open(f"{dir}/{count}.png", "wb") as fh:
            fh.write(base64.b64decode(img_data))
            count = count + 1
    toc = time.perf_counter()
    print(f"Took {toc - tic} | Saved to {dir}")
