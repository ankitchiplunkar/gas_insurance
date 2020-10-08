# Gas insurance
Code for insuring gas payments


Contract deployed at [0x14cddffad62e6b31f8091bb8e71707d5b6314f4a](https://ropsten.etherscan.io/address/0x14cddffad62e6b31f8091bb8e71707d5b6314f4a) on ropsten network.

1. Gas can be saved by having only 1 transaction for an ERC20 transfer.
2. Gas can be optimized by buying when its cheap and paying when it is costly.
3. Gas can also be released by destroying the contract while performing a transfer.

### Setup
```
pip install -r requirements.txt
```

### Estimated Gas costs

| Mode        | ETH Transfer           | ERC20 Transfer  |
| ------------- |:-------------:| -----:|
| Normal Operation      | 21000 | 72000 |
| Using Transfer Contract      | 30500      |   41000 |
| Using Transfer with Destruct | 17000      |   23000 |

To estimate gas costs locally run

```
brownie run scripts/local_gas_estimate.py
```