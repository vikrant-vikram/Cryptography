# sub = {}


import random

subE = {}
subD = {}

def subs():
    l1 = [chr(i) for i in range(32,127)]
    # l2 = [chr(i)for i in range(40,128)]

    random.shuffle(l1)
    counter = 0
    for i in range(32,127):
        subE[chr(i)] = l1[counter]
        subD[ l1[counter]] = chr(i)
        counter+=1





def encrypt(plainText):
    # shift(n)
    subs()
    cipher = ""
    print(subE)

    for i in plainText:
        cipher+=subE[i]
        # cipher += chr(ord(i)+n)
    return cipher

def decrypt(cipher):
    plainData = ""
    for i in cipher:
        plainData+=subD[i]
        # val = ord(i)-n
        # if(val <0):
        #     val+=128
        # plainData+=chr(val)
    return plainData



while(True):
    print("What do u want to perform : ")
    print("\t 1. Encrypt")
    print("\t 2. Decrypt")
    print("\t 3. Exit ( Default )")

    n = int(input("Enter Your responce : "))
    if( n == 1):
        # key = int(input("Enter your Shift Key : "))
        plainText = input("Enter your data which you want to Encrypt : ")
        cipher = encrypt(plainText)
        print("Your Encrypted data is ")
        print("-----------------------------Chipher -----------------------")
        print(cipher)
        print("--------------------------------------------------------------")
    elif( n == 2):
        # key = int(input("Enter your Shift Key : "))
        cipher = input("Enter your data which you want to Decrypt : ")
        plainText = decrypt(cipher)
        print("Your Decrypted data is ")
        print("-----------------------------Data -----------------------")
        print(plainText)
        print("--------------------------------------------------------------")
    else:
        break
