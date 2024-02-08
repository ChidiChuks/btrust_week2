To parse Bitcoin transaction hexes and identify the transaction type (Legacy, SegWit with RBF, Taproot), as well as extract version, inputs, outputs, and locktime, you'll need a parser that can handle the different transaction formats. Below, I'll provide a basic Python script using the bitcoinlib library for parsing Bitcoin transactions. This library provides functionality to handle various Bitcoin transaction types.

First, you'll need to install the library:
```pip install python-bitcoinlib```

Run from the command line with the transaction hex as an argument and the script `parse_transaction.py`:

```python parse_transaction.py <transaction_hex>```
