import requests
import json
import time
import os


#Lambda Server Url
my_key = 'your key here'
url = "https://lambda-treasure-hunt.herokuapp.com/api/adv"
headers = {"content-type": "application/json", "Authorization": f"Token {my_key}"}
cooldown = 0

#functions for requests to lambda server
def init_player():
    player_init = requests.get(f"{ url }/init", headers=headers)
    return player_init.json()


def move_player(direction):
    move = requests.post(f"{ url }/move", json={"direction": direction}, headers=headers)
    return move.json()

def take_treasure():
    pass

def sell_treasure():
    pass

def change_name():
    pass

print(move_player('s'))