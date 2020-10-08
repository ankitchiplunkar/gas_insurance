from brownie import accounts, Transfer, Token, GasToken
ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"
OWNER = accounts[0]

def main():
    token = Token.deploy("Test Token", "TST", 18, 1e20, {'from': accounts[1]})

    transfer = Transfer.deploy({"from": accounts[0]})
    print(f"Gas used to deploy the contract {transfer.tx.gas_used}")

    t = accounts[0].transfer(transfer.address, 10**18)
    print(f"Gas used to pay ETH {t.gas_used}")

    t = transfer.transfer(ZERO_ADDRESS, accounts[1], 10**17, {'from': accounts[0]})
    print(f"Gas used to pay ETH using the contract contract {t.gas_used}")

    t = transfer.transferAndDestruct(ZERO_ADDRESS, accounts[1], 10**17, {'from': accounts[0]})
    print(f"Gas used to pay ETH by destoying the contract {t.gas_used}")

    # Token gas usage
    transfer = Transfer.deploy({"from": accounts[0]})
    t = token.transfer(transfer.address, 10**18, {'from':accounts[1]})
    print(f"Gas used to send ERC20 to a contract {t.gas_used}")

    t = transfer.transfer(token.address, accounts[1], 10**17, {'from': accounts[0]})
    print(f"Gas used to send ERC20 using the contract {t.gas_used}")

    t = transfer.transferAndDestruct(token.address, accounts[1], 10**17, {'from': accounts[0]})
    print(f"Gas used to send ERC20 by destoying the contract {t.gas_used}")
