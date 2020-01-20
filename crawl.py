import requests
import json
token = ""
key = ""
after = ""
data = ""
name = ""
URL = 'https://openapi.band.us/v2/band/posts'
for i in range(1,16):
    if after == "":
        params = {'access_token': token, 'band_key': key}
        response = requests.get(URL, params=params)
        for i in response.json()['result_data']['items']:
            if i['author']['name']==name:
                data += i['content']
                data += "\n"
        after = response.json()['result_data']['paging']['next_params']['after']
        data+="\n\n"
    else:
        params = {'access_token': token, 'band_key': key, 'after': after}
        response = requests.get(URL, params=params)
        for i in response.json()['result_data']['items']:
            if i['author']['name']==name:
                data += i['content']
                data += "\n"
        after = response.json()['result_data']['paging']['next_params']['after']
        print(response.json()['result_data']['paging']['next_params'])
        data += "\n\n"
# json_str = json.dumps(response.json(), ensure_ascii=False, indent=4)
# with open("last"+".json", 'w',encoding='utf-8') as f:
#      f.write(json_str)
with open("full contents"+".txt", 'w',encoding='utf-8') as f:
    f.write(data)