



def keySteamGenerator(key):
    keyStream = ""
    return keyStream
def encrypt(plaintext , keyStream):
    cipher = ""
    return cipher
def decrypt(cipher, keyStream):
    plainText = ""
    return plainText




while(True):
    print("What do u want to perform : ")
    print("\t 1. Encrypt")
    print("\t 2. Decrypt")
    print("\t 3. Exit ( Default )")

    n = int(input("Enter Your responce : "))
    if( n == 1):
        key = int(input("Enter your Shift Key : "))
        plainText = input("Enter your data which you want to Encrypt : ")
        cipher = encrypt(plainText, key)
        print("Your Encrypted data is ")
        print("-----------------------------Chipher -----------------------")
        print(cipher)
        print("--------------------------------------------------------------")
    elif( n == 2):
        key = int(input("Enter your Shift Key : "))
        cipher = input("Enter your data which you want to Decrypt : ")
        plainText = decrypt(cipher, key)
        print("Your Decrypted data is ")
        print("-----------------------------Data -----------------------")
        print(plainText)
        print("--------------------------------------------------------------")
    else:
        break
