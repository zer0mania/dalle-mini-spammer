import json
import base64
import time
import os
import requests

while True:
    prompt = input("Enter prompt: ")
    print("Generating..")
    while True:
        url = "https://bf.dallemini.ai:443/generate"
        headers = {"Sec-Ch-Ua": "\"-Not.A/Brand\";v=\"8\", \"Chromium\";v=\"102\"", "Accept": "application/json", "Content-Type": "application/json", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://hf.space", "Sec-Fetch-Site": "cross-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://hf.space/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
        json = {"prompt": f"{prompt}"}
        response = requests.post(url, headers=headers, json=json)
        if "mega-1:v16" in response.text:
            break

    data = response.json()

    count = 0
    current_time = str(int(time.time()))

    os.mkdir(current_time)

    for i in data["images"]:
        img_data = i.replace('\n','')
        with open(f"{current_time}/{count}.png", "wb") as fh:
            fh.write(base64.b64decode(img_data))
            count = count + 1
    print(f"Saved to {current_time}")
    