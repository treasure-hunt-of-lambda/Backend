import hashlib
import requests
import json
import time


def valid_proof(last_proof, proof, difficulty):
    """
    Validates the Proof:  Does hash(last_proof, proof) contain 4
    leading zeroes?
    """
    zeroes = [0] * difficulty
    lead = "".join(map(str,zeroes))
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:difficulty] == lead


def proof_of_work(last_proof, difficulty):
    """
    Simple Proof of Work Algorithm
    - Find a number p' such that hash(pp') contains 4 leading
    zeroes, where p is the previous p'
    - p is the previous proof, and p' is the new proof
    """

    proof = 0
    while valid_proof(last_proof, proof, difficulty) is False:
        proof += 1

    return proof

player_key = '7d6fdac551c4a8667047bc1eb7250d86c4163c01'
url = "https://lambda-treasure-hunt.herokuapp.com/api/bc/"
headers = {"content-type": "application/json", "Authorization": f"Token {player_key}"}

def get_lambda_proof():
    r = requests.get(f'{url}/last_proof', headers=headers)
    time.sleep(r.json()['cooldown'])
    return r

def mining(new):
    r = requests.post(f'{url}/mine', json={"proof":new}, headers=headers)
    time.sleep(r.json()['cooldown'])
    return r

def balance():
    r = requests.get(f'{url}/get_balance', headers=headers)
    time.sleep(r.json()['cooldown'])
    return r
    


    # last_proof = get_lambda_proof().json()
    # data = {}
    # data['last_proof'] = last_proof['proof']
    # data['difficulty'] = last_proof['difficulty']

    # new_proof = proof_of_work(data['last_proof'], last_proof['difficulty'])
    # print(data)
    # print(new_proof)

    # post_proof = mining(new_proof)

    # print(post_proof.json())
print(balance().json())

while True:
    last_proof = get_lambda_proof().json()
    data = {}
    data['last_proof'] = last_proof['proof']
    data['difficulty'] = last_proof['difficulty']
    # data['difficulty'] = 3

    print('This is the previous lambda proof')
    print(last_proof)
    print(data)
    print('making new proof')
    new_proof = proof_of_work(data['last_proof'], data['difficulty'])
    print('You made a new proof!')
    print(new_proof)
    print('Time to mine')
    post_proof = mining(new_proof)
    print('You mined something...maybe..')
    print(post_proof.json())
    


# ha = [0] * 9
# res = "".join(map(str, ha)) 
# print(str(res))