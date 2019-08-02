import hashlib
import requests
import sys
import time

def proof_of_work(last_proof):
    print("Searching for next proof")
    proof = 4844660
    while valid_proof(last_proof, proof) is False:
        proof += 1
    print("Proof found: " + str(proof))
    return proof

def valid_proof(last_proof, proof):
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:7] == "0000000"

if __name__ == '__main__':

    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-treasure-hunt.herokuapp.com/api/bc"
    coins_mined = 0

    # Run forever until interrupted
    while True:
       
        headers = {"content-type": "application/json", "Authorization": "Token d4bd4d2ca313d3c704b851ece19ecfcf72984f1b"}
        r = requests.get(f"{node}/last_proof", headers=headers)
        data = r.json()
        last_proof = data['proof']
        new_proof = proof_of_work(last_proof)

        post_data = {"proof": new_proof}
        r = requests.post(f"{node}/mine", json=post_data, headers=headers)
        data = r.json()
        print(data)
        time.sleep(6)

        if data.get('messages') == 'New Block Forged':
       
            coins_mined += 1

            print("Total coins mined: ", coins_mined)
        else:
            print(data.get('messages'))