


import requests
import re
import json

url = 'https://www.toutiao.com/a6514487262179230212/#p=2'

content = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}).text
data = re.findall('JSON\.parse\(([\s\S]*?)\),', content)[0]
js_obj = json.loads(json.loads(data))
tmp_url_list = []
for i in range(len(js_obj['sub_images'])):
    tmp_data = js_obj['sub_images'][i]['url_list'][0]['url']
    tmp_url_list.append(tmp_data)
for list in tmp_url_list:
    print(list)