from brownie import Transfer, accounts

acct = accounts.load("gas_insurance")

def main():
    transfer = Transfer.deploy({"from": acct})