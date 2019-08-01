import requests
import json
import time
import os
import random
# from queue import Queue

#Lambda Server Url
my_key = 'd4bd4d2ca313d3c704b851ece19ecfcf72984f1b'
url = "https://lambda-treasure-hunt.herokuapp.com/api/adv"
headers = {"content-type": "application/json", "Authorization": f"Token {my_key}"}
cooldown = 0

#functions for requests to lambda server
def init_player():
    player_init = requests.get(f"{ url }/init", headers=headers)
    return player_init.json()

def move_player(direction):
    move = requests.post(f"{ url }/move", json={"direction": direction}, headers=headers)
    data = move.json()
    print(data)
    time.sleep(data["cooldown"])
    return  data

def take_treasure():
    pass

def sell_treasure():
    pass

def change_name():
    pass



print(move_player('n'))


