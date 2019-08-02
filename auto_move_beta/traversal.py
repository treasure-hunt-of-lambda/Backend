from queue import Queue
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

# class Queue():
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, value):
#         self.queue.append(value)
#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None
#     def size(self):
#         return len(self.queue)
#functions for requests to lambda server
# def init_player():
#     player_init = requests.get(f"{ url }/init", headers=headers)
#     return player_init.json()

<<<<<<< HEAD:auto_move_beta/traversal.py
def move_player(direction):
    move = requests.post(f"{ url }/move", json={"direction": direction}, headers=headers)
    data = move.json()
    print(data)
    time.sleep(data["cooldown"])
    return  data
=======

# def move_player(direction):
#     move = requests.post(f"{ url }/move", json={"direction": direction}, headers=headers)
#     return move.json()
>>>>>>> master:traversal.py

# def take_treasure():
#     pass

# def sell_treasure():
#     pass

# def change_name():
#     pass

# print(move_player('s'))
# # print(init_player())
# # print(move_player('e'))
# print(move_player('n'))
# # print(move_player('w'))



# Fill this out
traversalPath = []

# base_url = "https://lambda-treasure-hunt.herokuapp.com/api/adv"
# headers = {"Authorization": "Token 3b5ce4bde563d93d6ab89e3b8b9afd874e87f196"}

def travel(dir):
    r = requests.post(f"{url}/move/", headers = headers, json= {"direction": dir}) 
    data = r.json()
    print(data)
    time.sleep(data["cooldown"])
    return  data

# [] to {}
def transform_exits(exits):
    dict = {}
    for ext in exits:
        dict[ext] = '?'
    return dict

# get nearest room with ? unknown exit (bfs)
def get_pivot_room(explored_map, starting_room):
    visited = []
    q = Queue()
    q.put([(starting_room, '?')])
    while not q.empty():
        new_room_path = q.get()
        new_room = new_room_path[-1]
        for dir, ext in explored_map[new_room[0]].items():
            if ext == '?':
                return new_room_path

        if new_room[0] not in visited:
            visited.append(new_room[0])
            for exit_dir, exit in explored_map[new_room[0]].items():
                new_path = new_room_path[::]
                new_path.append((exit, exit_dir))
                q.put(new_path)
    return [-1]

def back_track(map, current_room, trav_path):
    return_val = [False]

    pivot_room_path = get_pivot_room(map, current_room)
    if pivot_room_path[-1] == -1:
        done = True
        return_val[0] = done
    else:
        for i in range(len(pivot_room_path)):
            if pivot_room_path[i] != '?':
                travel(pivot_room_path[i])
                trav_path.append(pivot_room_path[i])
        
        if pivot_room_path[-1][0] >= 0:
            current_room = pivot_room_path[-1][0]
            return_val.append(current_room )
        
        # else:
        #      travel(pivot_room_path)
    return return_val


r = requests.get(url = f"{url}/init/", headers = headers) 
init_data = r.json()
time.sleep(init_data["cooldown"])
print(json.dumps(init_data, indent=4))

explored_map = {}
explored_map[init_data["room_id"]] = transform_exits(init_data["exits"])

current_room = init_data["room_id"] 


done = False

complement_dirs = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

while not done:
    # track number of exits
    # pass
    counter = 0  
    for dir, ext in explored_map[current_room].items():
        counter += 1
        if ext == '?':
            player = travel(dir)
            print('stuck at here: 1')
            # check for loop
            room_id = player["room_id"] 
            if  room_id in explored_map.keys():
                # add room num as exit to prev room
                # prev room is 'currentrRoom' in this case because current_room var is not updated yet
                explored_map[current_room][dir] = room_id
                # go back to prev room
                print('stuck ')
                travel(complement_dirs[dir])

                back_track_vals = back_track(explored_map, current_room, traversalPath)
                if back_track_vals[0]:
                    done = True
                else:
                    current_room = back_track_vals[1]
            else:
                traversalPath.append(dir)
                new_room = room_id
                explored_map[current_room][dir] = new_room 
                explored_map[new_room] = transform_exits(player["exits"]) 
                explored_map[new_room][complement_dirs[dir]] = current_room
                current_room = new_room
            break
        # a dead end
        elif counter == len(explored_map[current_room]): 
            print('1', f'{explored_map[current_room]}')
            back_track_vals = back_track(explored_map, current_room, traversalPath)
            if back_track_vals[0]:
                print('3', back_track_vals[0])
                done = True
            else:
                current_room = back_track_vals[1]

with open('map.json', 'w', encoding='utf-8') as f:
    json.dump(explored_map, f, ensure_ascii=False, indent=4)

# curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"shiny treasure"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/take/

<<<<<<< HEAD:auto_move_beta/traversal.py


print(move_player('n'))


=======
>>>>>>> master:traversal.py
