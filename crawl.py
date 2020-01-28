import requests
import json
import os
token = ""
key = ""
after = ""
data = ""
dataforall =""
name = ""
URL = 'https://openapi.band.us/v2/band/posts'
for i in range(0,800):
    if after == "":
        params = {'access_token': token, 'band_key': key}
        response = requests.get(URL, params=params)
        for i in response.json()['result_data']['items']:
            if i['author']['name']==name:
                dataforall += i['content']
                dataforall += "\n"
                data = i['content']
                with open(os.getcwd() + "/txt/" + i['post_key'] + ".txt", 'w', encoding='utf-8') as f:
                    f.write(data)
        after = response.json()['result_data']['paging']['next_params']['after']
        dataforall+="\n\n\n\n-----------------------------"
    else:
        params = {'access_token': token, 'band_key': key, 'after': after}
        response = requests.get(URL, params=params)
        for i in response.json()['result_data']['items']:
            if i['author']['name']==name:
                dataforall += i['content']
                dataforall += "\n"
                data = i['content']
                with open(os.getcwd() + "/txt/" + i['post_key'] + ".txt", 'w', encoding='utf-8') as f:
                    f.write(data)
        after = response.json()['result_data']['paging']['next_params']['after']
        print(response.json()['result_data']['paging']['next_params'])
        dataforall += "\n\n\n\n-----------------------------"
# params = {'access_token': token, 'band_key': key}
# response = requests.get(URL, params=params)
# json_str = json.dumps(response.json(), ensure_ascii=False, indent=4)
# with open("last"+".json", 'w',encoding='utf-8') as f:
#     f.write(json_str)
with open("full contents"+".txt", 'w',encoding='utf-8') as f:
    f.write(dataforall)