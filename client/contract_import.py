from web3 import Web3, HTTPProvider, TestRPCProvider
from web3.contract import ConciseContract
#from solc import compile_source
import json
import sys

class contractImport():
    def __init__(self, path="Smallbank.json"):
        self.w3 = Web3(HTTPProvider())
        self.path = "../build/contracts/"+path
    def new(self, deployer, gas, isConcise=True):
        #deployer = args[0]
        #gas = args[1]
        """
        with open("../contracts/Smallbank.sol", "r") as f:
            compiled_sol = compile_source(f.read())
            contract_interface = compiled_sol['<stdin>:Smallbank']
        """
        with open(self.path, "r") as f:
            contract_json = json.loads(f.read())
        contract_abi, contract_bytecode = contract_json["abi"], contract_json["bytecode"]
        contract = self.w3.eth.contract(
                abi=contract_abi,
                bytecode=contract_bytecode
        )
        
        tx_hash = contract.constructor().transact(transaction=None)
        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)

        contract_instance = self.w3.eth.contract(
                address=tx_receipt.contractAddress,
                abi = contract_abi
        )
        
        if isConcise:
            concise_instance = ConciseContract(contract_instance)
            return concise_instance
        return contract_instance

    def deployed(self, address):
        with open(self.path, "r") as f:
            contract_json = json.loads(f.read())
        contract_abi = contract_json["abi"]

        contract_instance = w3.eth.contract(contract_abi, address, ContractFactoryClass=ConciseContract)
        return contract_instance

if __name__ == "__main__":
    w3 = Web3(HTTPProvider())
    ctrt = contractImport(path="Smallbank.json").new(w3.eth.accounts[0], 400000)




