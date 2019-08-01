import hashlib
import requests
import time
import sys

my_key = 'd4bd4d2ca313d3c704b851ece19ecfcf72984f1b'
url = "https://lambda-treasure-hunt.herokuapp.com/api/adv"
headers = {"content-type": "application/json", "Authorization": f"Token {my_key}"}

def proof_of_work(last_proof):
    print("Searching for next proof")
    proof = 96672155
    while valid_proof(last_proof, proof) is False:
        proof += 1

    print("Proof found: " + str(proof))
    return proof

def valid_proof(last_proof, proof):
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:6] == "000000"

if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-treasure-hunt.herokuapp.com/api/bc"

    coins_mined = 0
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof", headers = headers)
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))
        post_data = {"proof": new_proof}

        r = requests.post(url=node + "/mine", headers = headers, json=post_data)
        data = r.json()
        print(data)
        time.sleep(data["cooldown"])

        if data.get('messages') == 'New Block Forged':

            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('messages'))