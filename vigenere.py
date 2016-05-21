from argparse import ArgumentParser
from collections import Counter
parser = ArgumentParser()
parser.add_argument('max_keylength')
parser.add_argument('cipher_text')
parser.add_argument('encrypted_files',nargs='+')
args = parser.parse_args()

print "VIGENERE CRACKER\n"


ciphertexts=[]
cipher_text = args.cipher_text
with open("./"+cipher_text,'r') as fid:
	cipher_text = fid.read().replace(" ","").replace('\n','')

for arg in args.encrypted_files:
	with open("./"+arg,'r') as fid:
		ciphertexts.append(fid.read().replace(" ",""))


for i in xrange(1,int(args.max_keylength)+1):
	print "--------------------------\n"
	keystr=''
	for m in xrange(0,i):
		splitcipher=''
		for cipher in ciphertexts:
			j =0
			for x in cipher:
				if j%i==m:
					splitcipher+=x			
				j+=1	
		c = Counter(splitcipher)
		mc=c.most_common()
        	let,_ = mc[0]
		num = (ord(let)-65-ord('E')-65)%26
        	key = chr(num+65)
        	keystr+=(key)
	print "keystring: "+keystr+"\n"
	plaintext=''
	oldlen = len(keystr)
	keystrN=''
#	if oldlen > len(cipher_text):
#		print "KEY LONGER THAN CIPHERTEXT\n"
#	else:
	i=0
	while len(keystrN)!=len(cipher_text):
		keystrN+=keystr[i%oldlen]
		i+=1
	if len(keystr)>len(cipher_text):
		print "KEY TRUNCATED!\n"
	print "key used: "+keystrN+"\n"
	for x,y in zip(cipher_text,keystrN):
		plaintext+= chr((ord(x)-65-ord(y)-65)%26+65)
	print "plaintext: "+plaintext+"\n"
