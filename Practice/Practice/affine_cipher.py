# sub = [-1 for i in range(128)]
# sub = {}
# print("Chose Option\n")
# print("\t 1. Enter Shift Value \n")
# print("\t 2. Default")
# n =input(" Enter Shift Value")

# def shift(n):
#     for i in range(128):
#         sub[i] = (i+n)%128





def encrypt(plainText, a, b):
    # shift(n)
    # print(sub)
    cipher = ""
    for i in plainText:

        cipher += (chr((((ord(i)-ord("a"))*a)+b)%26))
    return cipher

def decrypt(cipher, a, b):
    plainData = ""
    for i in cipher:
        val = ord(i)-n
        if(val <0):
            val+=128
        plainData+=chr(val)
    return plainData



while(True):
    print("What do u want to perform : ")
    print("\t 1. Encrypt")
    print("\t 2. Decrypt")
    print("\t 3. Exit ( Default )")

    n = int(input("Enter Your responce : "))
    if( n == 1):
        a = int(input("Enter your 'a' : "))
        b = int(input("Enter your 'b' : "))

        plainText = input("Enter your data which you want to Encrypt : ")
        cipher = encrypt(plainText, a, b)
        print("Your Encrypted data is ")
        print("-----------------------------Chipher -----------------------")
        print(cipher)
        print("--------------------------------------------------------------")
    elif( n == 2):
        a = int(input("Enter your 'a' : "))
        b = int(input("Enter your 'b' : "))
        cipher = input("Enter your data which you want to Decrypt : ")
        plainText = decrypt(cipher, a, b)
        print("Your Decrypted data is ")
        print("-----------------------------Data -----------------------")
        print(plainText)
        print("--------------------------------------------------------------")
    else:
        break
