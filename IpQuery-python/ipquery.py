import requests
import json
import os
import time
from fake_useragent import UserAgent


ua = UserAgent()
headers = {'User-Agent': ua.random}

menu = """\033[36m
▪   ▄▄▄·    .▄▄▄  ▄• ▄▌▄▄▄ .▄▄▄   ▄· ▄▌
██ ▐█ ▄█    ▐▀•▀█ █▪██▌▀▄.▀·▀▄ █·▐█▪██▌
▐█· ██▀·    █▌·.█▌█▌▐█▌▐▀▀▪▄▐▀▀▄ ▐█▌▐█▪
▐█▌▐█▪·•    ▐█▪▄█·▐█▄█▌▐█▄▄▌▐█•█▌ ▐█▀·.
▀▀▀.▀       ·▀▀█.  ▀▀▀  ▀▀▀ .▀  ▀  ▀ • 

1- Ip Query
2- Github
3- Exit
"""

def countdown(seconds):
    while seconds > 0:
        print(f"\033[33mTime remaining: {seconds} seconds\033[0m", end='\r')
        time.sleep(1)
        seconds -= 1

    print("\nCountdown complete!")

def menu_start():
    os.system("cls||clear")
    print(menu)

def ipİnfo():
    menu_start()
    choose = int(input("\033[36mPlease select an option: \033[0m"))

    if choose == 1:
        ipaddress = input("\033[36mEnter the any Ip Address: \033[0m")
        fields = [
            'status', 'continent', 'continentCode', 'country', 'countryCode',
            'region', 'regionName', 'city', 'district', 'zip', 'lat', 'lon',
            'timezone', 'isp', 'org', 'as', 'asname', 'reverse', 'mobile',
            'proxy', 'hosting', 'query'
        ]
        url = f"http://ip-api.com/json/{ipaddress}?fields={','.join(fields)}"

        response = requests.get(url, headers=headers) # Make Requests
        data = response.json()
        data = {'author': 'xberkay-o', **data}
        file_name = ipaddress + ".json"

        if response.status_code == 200:
            print("\033[35mRequests successfully")
            try:
                # Create and Save File
                with open(file_name, "w") as json_file:
                    json.dump(data, json_file, indent=4)
                    print(f"\033[32mThe file named {file_name} has been saved")
            except:
                print("\033[31mFile creation failed")
        else:
            print("\033[31mRequest failed")
        
        countdown(3)
    elif choose == 2:
        os.system("cls||clear")
        print("\033[35mGithub: \033[37mhttps://github.com/xberkay-o")
        input("\n\033[31mIf you want to return to the main menu press enter...")
    elif choose == 3:
        print("Exiting... Thank you for use my application")
        countdown(2)
        os.system("cls||clear")
        exit()
        

while True:
    ipİnfo()
