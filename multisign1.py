from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

bitcoin = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(rpc_user, rpc_password))

add = dict()
privkey = dict()
pubkey = dict()
mid = "\",\"" #this thing inserts these 3 characters ","


for i in range(0, 3): #Generate three new addresses (Pub Key & Priv Key)
    print ()
    print ("Brand New Address Pair: Number", i+1)
    
    add[i] = bitcoin.getnewaddress()
    print ("Compressed Public Address -",len(add[i]),"chars -", add[i])
    
    privkey[i] = bitcoin.dumpprivkey(add[i])
    print ("Private Key -", len(privkey[i]),"chars -",privkey[i])

    validDate = bitcoin.validateaddress(add[i]) # we need a less compressed Public Key so we have to call validateaddress to find it
    pubkey[i] = validDate["pubkey"]
    print ("Less compressed Public Key/Address -",len(pubkey[i]),"chars -",pubkey[i])

print ()
print ("For fun you can paste this into bitcoind to verify multisig address")
print ("%s%s%s%s%s%s%s" % ('bitcoind createmultisig 2 \'["',pubkey[0],mid,pubkey[1],mid,pubkey[2],'"]\''))

print()
threeaddy = [pubkey[0],pubkey[1],pubkey[2]]
print ("The multisig address is")
multisigaddy = bitcoin.addmultisigaddress(2,threeaddy)
multiaddyandredeem = (bitcoin.createmultisig(2,threeaddy))
print (len(multisigaddy),"chars - ", multisigaddy)
print ()
print ("The redeemScript -", len(multiaddyandredeem["redeemScript"]), "chars -",multiaddyandredeem["redeemScript"])
print  ()
print ("Now copy all this output text and save it so you'll be ready for part two.")
print ("Also, you can send a tiny amt of bitcoins to this multisig address",multisigaddy,"to fund it,")
print ("Next time we'll go through all the steps to spend from your new multisig address.")


bitcoin = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(rpc_user, rpc_password)) #creates an object called 'bitcoin' that allows for bitcoind calls

add = dict()
privkey = dict()
pubkey = dict()
mid = "\",\"" #this thing inserts these 3 characters ","


for i in range(0, 3): #Generate three new addresses (Pub Key & Priv Key)
    print ()
    print ("Brand New Address Pair: Number", i+1)
    
    add[i] = bitcoin.getnewaddress()
    print ("Compressed Public Address -",len(add[i]),"chars -", add[i])
    
    privkey[i] = bitcoin.dumpprivkey(add[i])
    print ("Private Key -", len(privkey[i]),"chars -",privkey[i])

    validDate = bitcoin.validateaddress(add[i]) # we need a less compressed Public Key so we have to call validateaddress to find it
    pubkey[i] = validDate["pubkey"]
    print ("Less compressed Public Key/Address -",len(pubkey[i]),"chars -",pubkey[i])

print ()
print ("For fun you can paste this into bitcoind to verify multisig address")
print ("%s%s%s%s%s%s%s" % ('bitcoind createmultisig 2 \'["',pubkey[0],mid,pubkey[1],mid,pubkey[2],'"]\''))

print()
threeaddy = [pubkey[0],pubkey[1],pubkey[2]]
print ("The multisig address is")
multisigaddy = bitcoin.addmultisigaddress(2,threeaddy)
multiaddyandredeem = (bitcoin.createmultisig(2,threeaddy))
print (len(multisigaddy),"chars - ", multisigaddy)
print ()
print ("The redeemScript -", len(multiaddyandredeem["redeemScript"]), "chars -",multiaddyandredeem["redeemScript"])
print  ()
print ("Now copy all this output text and save it so you'll be ready for part two.")
print ("Also, you can send a tiny amt of bitcoins to this multisig address",multisigaddy,"to fund it,")
print ("Next time we'll go through all the steps to spend from your new multisig address.")
