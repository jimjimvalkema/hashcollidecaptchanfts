import webbrowser
from web3 import Web3
from solcx import install_solc
from solcx import compile_source
from itertools import combinations_with_replacement
import random


def getCaptcha(string):
	'''
	goes through every id and calls the mint function. prints the 
	solution, id and transaction data
	'''
	for i in range(1,10000):
		try:
			contract_instance.functions.mintCaptcha(i, string).call()
		except Exception as e:
			if not (str(e) == "execution reverted: Captcha Already Solved" or str(e) == "execution reverted: Incorrect Captcha"):
				webbrowser.get("firefox").open("https://api.thecaptcha.art/images/"+str(i))
				print(i, string)
				try:
					print("send 0.05 ETH to {} and add this to the hex field in metamask: {}".format(contract_address,get_tx_data(i,string,pers_addr)['data']))
				except Exception as e2:
					print(e2)
				print(e)
				if not str(e) == "execution reverted: Wrong Eth Amount":
					break

alphanumeric = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'.lower()
def adseed(s):
	'''
	adds randon characters to ur string 
	'''
	l = []
	#up this number if you cant find a solution or down it if you want a smaller solution/title :)
	n = 8 #4 - len(s)
	for j in range(0,n):
		for i in combinations_with_replacement(list(alphanumeric),j):
			l.append(s + str(i).replace(" ","").replace("(","").replace(")","").replace(",","").replace("'",""))

	random.shuffle(l)
	return l	
	
	
def getCaptchaList(l):
	for i in l:
		getCaptcha(i)

def brute_force_id(cap_id, end_char):
	'''
	tries to find a solution to a specific id and
	'''
	rando_shit = adseed(end_char)
	for i in rando_shit:
		try:
			contract_instance.functions.mintCaptcha(cap_id, i).call()
			print("trying {} with {}".format(cap_id, i))
		except Exception as e:
			if not (str(e) == "execution reverted: Captcha Already Solved" or str(e) == "execution reverted: Incorrect Captcha"):
				webbrowser.get("firefox").open("https://api.thecaptcha.art/images/"+str(cap_id))
				print(cap_id, i)
				if not str(e) == "execution reverted: Wrong Eth Amount":
					print("found "+cap_id+"but was already minted")
					print(e)
					continue
				else:
					print("done found it")
					break

def get_tx_data(cap_id, solution, addr_from):
	'''because etherscan hates emojis :)'''
	data = contract_instance.functions.mintCaptcha(cap_id, solution).buildTransaction(
	{"value" : 50000000000000000, "from" : addr_from})
	return data

#setup
install_solc(version='latest')
abi = """[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"string","name":"name","type":"string"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[],"name":"Published","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"MAX_SUPPLY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PRICE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"contractURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getSolvedCaptchas","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"string","name":"solution","type":"string"}],"name":"mintCaptcha","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"publish","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"published","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"scriptJson","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"prefix","type":"string"}],"name":"setBaseCaptchaURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"prefix","type":"string"}],"name":"setBaseURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes","name":"hashes","type":"bytes"}],"name":"setCaptchaHashes","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"script","type":"string"}],"name":"setGeneratorScript","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes","name":"solves","type":"bytes"}],"name":"setSolvedCaptchas","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"solvedCaptchaBytes","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenCaptchaURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"tokenIdToMetadata","outputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"address","name":"creator","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]"""
contract_address = "0x3d3D9cC92dBA4559D0f862E34fAA33E9967f6534"



############################
#start here
#Change this if dont have a local node!
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
#w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/891310e614d7438f9b26f7adc8d8cf47'))

#more setup igonore pls
contract_instance = w3.eth.contract(address=contract_address, abi=abi)

# input ur personal addres (needs enough eth)
pers_addr = "0x23bc95F84BD43C1FCc2bc285fDa4Cb12f9AEE2df"

#direct matches (ex "cool" and "kewl")
getCaptchaList(['❤️', '🖤', '🤍'])

#ends with (ex fsa3cool, 3ecool, afhcool, etc)
brute_force_id(7612,'💛')

#render tx data
print(get_tx_data(1302, "🤮", "0x23bc95F84BD43C1FCc2bc285fDa4Cb12f9AEE2df"))
