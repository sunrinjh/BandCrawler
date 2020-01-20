#https://openapi.band.us/v2/band/album/photos
import requests
import json
import urllib.request
import os
token = ""
key = ""
after = ""
data = ""
name = ""
URL = 'https://openapi.band.us/v2/band/album/photos'
for i in range(1,2):
    if after == "":
        params = {'access_token': token, 'band_key': key}
        response = requests.get(URL, params=params)
        for i in response.json()['result_data']['items']:
            if i['author']['name'] == name:
                urllib.request.urlretrieve(i['url'], os.getcwd() + "/img/" + i['photo_key'] + ".jpg")
                data += i['url']
                data += "\n"
        after = response.json()['result_data']['paging']['next_params']['after']
        data+="\n\n"
    else:
        params = {'access_token': token, 'band_key': key, 'after': after}
        response = requests.get(URL, params=params)
        for i in response.json()['result_data']['items']:
            if i['author']['name'] == name:
                urllib.request.urlretrieve(i['url'], os.getcwd() + "/python3/img/" + str(i) + "2.jpg")
                data += i['url']
                data += "\n"
        after = response.json()['result_data']['paging']['next_params']['after']
        print(response.json()['result_data']['paging']['next_params'])
        data += "\n\n"
# params = {'access_token': token, 'band_key': key}
# response = requests.get(URL, params=params)
# json_str = json.dumps(response.json(), ensure_ascii=False, indent=4)
# with open("lastpic"+".json", 'w',encoding='utf-8') as f:
#      f.write(json_str)
with open("full contentspic"+".txt", 'w',encoding='utf-8') as f:
     f.write(data)