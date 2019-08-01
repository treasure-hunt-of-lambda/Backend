import requests
import json
import time
import os
import sys
import random
import datetime


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

player_key = '7d6fdac551c4a8667047bc1eb7250d86c4163c01'
url = "https://lambda-treasure-hunt.herokuapp.com/api/adv"
headers = {"content-type": "application/json", "Authorization": f"Token {player_key}"}
cooldown = 0
player = {}

#Player actions:

#Must have 1000 gold to change player's name
def name_change(name):
    change = requests.post(f"{ url }/change_name", json={"name": name, "confirm": "aye"}, headers=headers)
    return change

#initialize player 
def init():
    start = requests.get(f"{ url }/init", headers=headers)
    time.sleep(start.json()['cooldown'])
    return start

#move player
def move_player(direction):
    move = requests.post(f"{ url }/move", json={"direction": direction}, headers=headers)
    time.sleep(move.json()['cooldown'])
    return move

#pickup treasure
def pickup(treasure):
    pick = requests.post(f"{ url }/take", json={"name": treasure}, headers=headers)
    return pick

#selling for gold
def sell_item(item):
    sell = requests.post(
        f"{ url }/sell", json={"name": item, "confirm": "yes"}, headers=headers)
    return sell

def status():
     s = requests.post(f"{ url }/status", headers=headers)
     return s
        
    


traversalPath = []

graph_rooms = {}
moves = ['n', 's', 'e', 'w']
opposite_directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

# initialize = init().json()

# print(initialize['room_id'])

# player['current_room'] = initialize['room_id']
# player['exits'] = initialize['exits']

# def mapTraversal(player, move=''):
#     if len(graph_rooms) == 500:
#         return
    
#     current_room = player['current_room']
#     print(current_room)

#     if player['current_room'] not in graph_rooms:
#         graph_rooms[player['current_room']] = {}
#         for exit in player['exits']:
#             graph_rooms[player['current_room']][exit] = '?'
#             # print(graph_rooms[player['current_room']][exit])



# mapTraversal(player, move='')
# print(move_player('n').json())
# print(move_player('e').json())
# print(move_player('s').json())
# print(move_player('w').json())
# print(sell_item('great treasure').json())
# print(status().json())

# print(initialize)
# print(move_player('s').json())
# print(move_player('e').json())
# print(move_player('e').json())
# print(move_player('s').json())
# print(move_player('e').json())
# print(move_player('e').json())
# print(move_player('e').json())
# print(move_player('s').json())
# print(move_player('s').json())
# print(move_player('s').json())
# print(move_player('s').json())
# print(move_player('s').json())
# print(move_player('s').json())
# print(name_change('stuck_on_map_traversal'))






