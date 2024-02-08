# Exercises

1. Given the following transaction hexs:
- Legacy
- Segwit with RBF
- Taproot
build a transaction parser to identify the transaction type, extracting the version, inputs, outputs and the locktime.

2. Perform the stack evaluation of this Bitcoin script and indicate whether it will result in true or false: hex: '010101029301038801027693010487'. Your solution should output the op_codes and/or values.

3. Given the string 'Btrust Builders', whose bytes encoding is '427472757374204275696c64657273', which is our preimage, generate the redeem script in hex format for the given preimage. Note: redeem_script => OP_SHA256 <lock_hex> OP_EQUAL
- Derive an address with from the above (2) redeemscript and construct a transaction that send Bitcoins to the address
- Construct another transaction that spends from the above (3) transaction given that you have both locking and unlock scripts. Ideally, this would mean you write a transaction builder that constructs the transaction and outputs the transaction ID. Broadcast the transaction on you local bitcoin network via the CLI.

4. [BONUS]: Write tests to validate the methods in your transaction parser. Hint: Your parser should have methods to decode the version, inputs, outputs, and locktime of any given transaction.

5. [BONUS]: Write tests to validate the methods in your transaction builder.
