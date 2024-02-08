import base58
import hashlib

def hash160(s):
    sha = hashlib.sha256(s).digest()
    ripe = hashlib.new('ripemd160')
    ripe.update(sha)
    return ripe.digest()

redeem_script_bytes = bytes.fromhex(redeem_script_hex)
redeem_script_hash = hash160(redeem_script_bytes)
version = b'\x05'
address = base58.b58encode_check(version + redeem_script_hash).decode()
print("Address:", address)
