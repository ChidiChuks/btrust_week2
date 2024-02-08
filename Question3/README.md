# To accomplish the tasks described, we'll go step by step:

1. Generate the redeem script in hex format using the preimage 'Btrust Builders'.

2. Derive an address from the redeem script.

3. Construct a transaction that sends Bitcoins to the derived address.

4. Construct another transaction that spends from the previous transaction, given both locking and unlocking scripts.

5. Broadcast the second transaction on the local Bitcoin network via the CLI.

## Let's start with the first step:

1. Generate the redeem script in hex format: `redeem_script.py`

2. Derive an address from the redeem script:
Since the redeem script is a P2SH (Pay to Script Hash) script, we'll first hash the redeem script and then encode it with the version byte 0x05 for mainnet P2SH addresses. Then, we'll generate the corresponding address. `hash_p2sh.py`

3. Construct a transaction that sends Bitcoins to the derived address:
To construct a transaction, you'll need a funded Bitcoin wallet and access to an RPC interface to interact with a Bitcoin node. You can use libraries like `python-bitcoinlib` or bitcoinlib for constructing transactions programmatically.

4. Construct another transaction that spends from the previous transaction:
Similarly, you'll need a funded wallet and access to an RPC interface to spend the Bitcoins from the previous transaction. You'll construct the transaction with inputs referencing the previous transaction output and provide both the locking and unlocking scripts. `sendrawtransaction.py`

5. Broadcast the transaction on the local Bitcoin network via the CLI:
You can use the bitcoin-cli tool to broadcast the constructed transaction:
`bitcoin-cli sendrawtransaction <raw_transaction_hex>`
