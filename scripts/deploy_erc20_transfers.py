from brownie import Transfer, accounts, interface

USDC_ADDRESS = "0x07865c6E87B9F70255377e024ace6630C1Eaa37F"
usdc = interface.IERC20(USDC_ADDRESS)
acct = accounts.load("gas_insurance")


def main():
    transfer = Transfer.deploy({"from": acct})
    # send USDC to transfer contract
    balance = usdc.balanceOf(acct.address)
    t = usdc.transfer(transfer.address, balance, {'from': acct})
    # send USDC using the contract
    t = transfer.transfer(USDC_ADDRESS, acct, balance/2, {'from': acct})
    # send USDC using the contract and destrying it
    t = transfer.transferAndDestruct(USDC_ADDRESS, acct, balance/2, {'from': acct})