import json
import requests

def get_station_code():
    city = {}
    station_name_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
    station_name_param = {
        'station_version': 1.9053
    }
    r = requests.get(url=station_name_url, params=station_name_param, verify=False).text
    for i in r.split('@'):
        if len(i.split('|')) >= 3:
            city[i.split('|')[1]] = i.split('|')[2]
    with open('station_code.json', 'w', encoding='utf-8') as f:
        json.dump(city, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    get_station_code()
