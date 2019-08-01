from map import data
from helper_funcs import getPathToRoom
from helper_funcs import travel

from queue import Queue

import random
import json
import requests
import time

base_url = "https://lambda-treasure-hunt.herokuapp.com/api/adv"
headers = {"Authorization": "Token d4bd4d2ca313d3c704b851ece19ecfcf72984f1b"}


rooms = list(data.keys())

init = requests.get(f"{base_url}/init/", headers = headers) 
current_room_data = init.json()
current_room = f'{current_room_data["room_id"]}'
time.sleep(45)
while True:
	#get a random room to go to
	target_room = rooms[random.randrange(len(rooms)-1)]

	# set target_room to a specific room (shop, shrine, etc)
	# target_room = "467"
	# get the path, a list of directions eg ['s','n'...]
	path = getPathToRoom(data, current_room, target_room)

	# follow the path
	for dir in path:
		new_room_data = travel(data, current_room,dir)
		current_room = f'{new_room_data["room_id"]}'
		print(new_room_data)

	# after getting to the last dir, it gets another target room randomly