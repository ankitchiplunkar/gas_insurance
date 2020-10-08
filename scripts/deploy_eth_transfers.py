from brownie import Transfer, accounts

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"
acct = accounts.load("gas_insurance")

def main():
    transfer = Transfer.deploy({"from": acct})
    # send 1 ETH to transfer contract
    t = acct.transfer(transfer.address, 10**18)
    # send ETH using the contract
    t = transfer.transfer(ZERO_ADDRESS, acct, 10**17, {'from': acct})
    # send ETH using the contract and destrying it
    t = transfer.transferAndDestruct(ZERO_ADDRESS, acct, 10**17, {'from': acct})