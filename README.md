# hashcollidecaptchanfts  
A quick and dirty python script to find collisions on [TheCaptcha](https://www.thecaptcha.art/) nfts  
example: https://opensea.io/assets/0x3d3d9cc92dba4559d0f862e34faa33e9967f6534/4218

Use at your own risk! make sure you know what ur doing  

Tutorial (incomplete ish)  
Intall [python](https://www.python.org/downloads/)    
`sudo apt-get install python3.8`  

install libraries  
`pip3 install web3; pip3 install py-solc-x`    

set parameters   
Sorry didn't do arg parse yet so go to the end of the script to edit them 🙃  

run it:  
`python3 hashcollidecaptchas.py`   

it should return something like this when it finds something (just a example):   
```
9275 💰  
send 0.05 ETH to 0x3d3D9cC92dBA4559D0f862E34fAA33E9967f6534 and add this to the hex field in metamask: 0x68733aa20000003241001423  
execution reverted: Wrong Eth Amount  
```    

Then send 0.05 ETH to the captcha nft contract and add the hex data in metamask.   
Make sure to dubbel check the gaslimit and if it's not already minted!  

Extra notes:  
If you dont see the hex data field in metamask: click your profile icon and then go to settings>Show Hex Data  
you can ignore `execution reverted: Wrong Eth Amount` it's just to debug.  
Also this script would probably be a lott faster if you would hash it inside the script instead of doing calls to a full node!  
Also don't blindly run hex data from stranger! It can be a way to steal tokens/ETH!  
