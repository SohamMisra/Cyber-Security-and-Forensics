import random
prng=[]
strnascii=[]
cipher=[]
ciphertext=""
str_input=input("Enter the string:")
for i in range(0,len(str_input)):
    prng.append(random.randint(0,255));
for i in range(0,len(str_input)):
    strnascii.append(ord(str_input[i]))
for i in range(len(prng)):
    cipher.append(prng[i]^strnascii[i])
for i in range(0,len(prng)):
    ciphertext+=chr(cipher[i])
print(prng)
print("Ciphertext:",ciphertext)
with open("ciphertext.txt","w") as file:
    file.writelines(str(prng)+"\n")
    file.writelines(ciphertext)
