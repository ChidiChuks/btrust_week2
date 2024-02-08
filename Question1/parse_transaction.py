from bitcoin.rpc import Proxy
from bitcoin.core import lx, CTransaction
import sys

def parse_transaction(transaction_hex):
    tx = CTransaction()
    tx.deserialize(lx(transaction_hex))
    
    version = tx.nVersion
    inputs = []
    for txin in tx.vin:
        inputs.append({
            'prev_txid': txin.prevout.hash,
            'prev_output_index': txin.prevout.n,
            'script_sig': txin.scriptSig.hex(),
            'sequence': txin.nSequence
        })
    
    outputs = []
    for txout in tx.vout:
        outputs.append({
            'value': txout.nValue,
            'script_pubkey': txout.scriptPubKey.hex()
        })
    
    locktime = tx.nLockTime
    
    return {
        'version': version,
        'inputs': inputs,
        'outputs': outputs,
        'locktime': locktime
    }

def identify_transaction_type(transaction_hex):
    tx = CTransaction()
    tx.deserialize(lx(transaction_hex))
    
    if tx.is_coinbase():
        return 'Coinbase (Legacy)'
    
    has_segwit_input = any(txin.is_witness() for txin in tx.vin)
    if has_segwit_input:
        if tx.nVersion & (1 << 31):
            return 'SegWit with RBF'
        else:
            return 'SegWit'
    
    # For Taproot, you need to analyze the scriptPubKey of the outputs
    # This script is a basic demonstration and doesn't handle Taproot
    
    return 'Legacy'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_transaction.py <transaction_hex>")
        sys.exit(1)

    transaction_hex = sys.argv[1]
    transaction_type = identify_transaction_type(transaction_hex)
    parsed_transaction = parse_transaction(transaction_hex)

    print("Transaction Type:", transaction_type)
    print("Version:", parsed_transaction['version'])
    print("Inputs:")
    for index, input_data in enumerate(parsed_transaction['inputs']):
        print(f"Input {index+1}:")
        print("\tPrevious Transaction ID:", input_data['prev_txid'])
        print("\tPrevious Output Index:", input_data['prev_output_index'])
        print("\tScriptSig:", input_data['script_sig'])
        print("\tSequence:", input_data['sequence'])
    print("Outputs:")
    for index, output_data in enumerate(parsed_transaction['outputs']):
        print(f"Output {index+1}:")
        print("\tValue:", output_data['value'])
        print("\tScriptPubKey:", output_data['script_pubkey'])
    print("Locktime:", parsed_transaction['locktime'])

