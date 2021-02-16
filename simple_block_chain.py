import hashlib
import json
from time import time

class Blockchain(object):
    
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.new_block(previous_hash="harris bought 100 doge coin", proof=100)
        
# function to create new block
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

# Search the blockchain for the most recent block.

    @property
    def last_block(self):
 
        return self.chain[-1]

# add transaction  

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

# turn a block into a string and hash it with SHA256 encryption.

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

# initiate the blockchain 
bc = Blockchain()

# add new transaction and create a new block
tran1 = bc.new_transaction("Harris", "Mike", '110 DOGE')
bc.new_block(12345)

# print chain
print(bc.chain)
