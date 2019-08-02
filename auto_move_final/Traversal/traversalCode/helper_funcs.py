from queue import Queue

import requests
import time

# from map import data

base_url = "https://lambda-treasure-hunt.herokuapp.com/api/adv"
headers = {"Authorization": "Token d4bd4d2ca313d3c704b851ece19ecfcf72984f1b"}

def getPathToRoom(map, starting_room, target_room):
	visited = []
	q = Queue()
	q.put([(starting_room, 0)])
	while not q.empty():
		new_room_path = q.get()
		new_room = new_room_path[-1]
		if new_room[0] == target_room:
			return [item[1] for item in new_room_path[1:]]

		if new_room[0] not in visited:
			visited.append(new_room[0])
			for exit_dir, exit in map[f'{new_room[0]}'].items():
				new_path = new_room_path[::]
				new_path.append((f'{exit}', exit_dir))
				q.put(new_path)

# return travel data
def travel(map, current_room, dir):
	print(current_room, map[f'{current_room}'], dir)
	r = requests.post(f"{base_url}/move/", headers = headers, json= {"direction": dir, "next_room_id": f"{map[f'{current_room}'][dir]}"}) 
	print(r)
	data = r.json()
	time.sleep(data["cooldown"])
	return  data

def getStatus():
	r = requests.post(f"{base_url}/status/", headers = headers) 
	status = r.json()
	print(status)
	time.sleep(status["cooldown"])
	return status

def toStore(map, current_room):
	store_path = getPathToRoom(map, current_room, "1")
	current_room_data = {}
	room = current_room
	for dir in store_path:
		current_room_data = travel(map, room, dir)
		room = current_room_data["room_id"]
	return current_room_data

def sellItems(items):
	for item in items:
		r = requests.post(f"{base_url}/sell/", headers = headers, json = {"name": item, "confirm": "yes"}) 
		sell_data = r.json()
		time.sleep(sell_data["cooldown"])
		
def getItems(items):
	status = {}
	for item in items:
		r = requests.post(f"{base_url}/take/", headers = headers, json = {"name": item}) 
		sell_data = r.json()
		time.sleep(sell_data["cooldown"])
		status = getStatus()
		if status["encumbrance"] >= status["strength"]//2:
			break
	return status