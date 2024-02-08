from bitcoin.core import CTransaction, COutPoint, CTxIn, CTxOut
from bitcoin.core.script import CScript
from bitcoin.core.scripteval import VerifyScript, SCRIPT_VERIFY_P2SH

# Construct the spending transaction
tx = CTransaction()
tx.vin.append(CTxIn(COutPoint(prev_txid, prev_out_index), unlocking_script))
tx.vout.append(CTxOut(value, locking_script))

# Sign the transaction
# Note: You need to sign the transaction with your private key

# Serialize and print the transaction ID
txid = tx.GetTxid()
print("Transaction ID:", txid)

