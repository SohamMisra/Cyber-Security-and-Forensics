prng=[]
strnascii=[]
plain=[]
plaintext=""
with open("ciphertext.txt","r") as file:
    prng_raw=file.readline()
    prng=prng_raw.strip("][\n").split(",")
    ciphertext=file.readline()
    for i in range(len(prng)):
        strnascii.append(ord(ciphertext[i]))
for i in range(len(prng)):
    plain.append(chr(int(prng[i])^int(strnascii[i])))
for i in range(len(plain)):
    plaintext+=plain[i]
print("Plaintext:",str(plaintext))