import hashlib

preimage = b'Btrust Builders'
hash_preimage = hashlib.sha256(preimage).hexdigest()
redeem_script = f'OP_SHA256 {hash_preimage} OP_EQUAL'
redeem_script_hex = redeem_script.encode('utf-8').hex()
print("Redeem Script Hex:", redeem_script_hex)
