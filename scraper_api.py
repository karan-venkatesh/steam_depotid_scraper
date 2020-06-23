import json
from steam.client import SteamClient
from steam.client.cdn import CDNClient
from steam.enums.emsg import EMsg
import pandas as pd

#Source
#http://api.steampowered.com/ISteamApps/GetAppList/v0002/

mysteam = SteamClient()
mysteam.anonymous_login()

mycdn = CDNClient(mysteam)

count=0
info=[]

with open('steam_ids.json',encoding='utf-8') as json_file:
    data = json.load(json_file)
    counter=1000
    for entry in data['applist']['apps']:
        try:
            if counter < 1:
                counter = 1000
                out = pd.DataFrame(info)
                out.to_csv("depot_id_steam_checkpoint.csv")
            else:
                counter -= 1
            print(entry['appid'],entry['name'])
            data = mycdn.get_app_depot_info(int(entry['appid']))
            # print(data, type(data))
            for item in data:
                if item.isdigit():
                    # print(item,data[item]['name'],type(item))
                    info.append([entry['appid'],entry['name'], item, data[item]['name']])
        except:
            print("Could not find item ",entry['appid'],entry['name'])

out=pd.DataFrame(info)
out.to_csv("depot_id_steam_full.csv")




