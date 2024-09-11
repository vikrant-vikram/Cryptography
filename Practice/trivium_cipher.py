
# Contannt Field

from functools import partial


r1_base = 1
r2_base = 94
r3_base = 178
r1_cap = 93
r2_cap = 84
r3_cap = 111
#Registers




def hexToBin(hex_string, reg):
    integer_value = int(hex_string, 16)
    binary_string = format(integer_value, f'0{reg}b')
    return binary_string[::-1]

def loader(key, IV, r1, r2, r3):
    bin_key = str(hexToBin(key, 80))
    bin_iv = str(hexToBin(IV, 80))

    counter = 0
    for k in bin_key[2:]:
        k = int(k)
        r1[counter] = k
        counter+=1
    counter = 0
    for iv in bin_iv:
        iv = int(iv)
        r2[counter] = iv
        counter+=1
    r3[-1] = 1
    r3[-2] = 1
    r3[-3] = 1
    return r1, r2, r3


def xnor(a, b):
    if( a == b):
        return 1
    else:
        return 0


def keyStreamGenerator(r1, r2,  r3):
    # loader(key, iv)
    # print(len90)
    t1 = r1[66 - r1_base] ^ r1[ 93 - r1_base]
    t2 = r2[ 162 - r2_base] ^ r2[ 177 - r2_base]
    t3 = r3[ 243 - r3_base]  ^ r3[ 288 - r3_base]

    z = t1 ^ t2 ^ t3
    # print(r1, r2, r3)

    t1 = t1 ^ xnor(r1[ 91 - r1_base], r1[ 92 - r1_base]) ^ r2 [171 - r2_base]
    t2 = t2 ^ xnor(r2[175 - r2_base],r2[176 - r2_base] ) ^ r3[264 - r3_base]
    t3 = t3 ^ xnor( r3[286 - r3_base],r3[267 - r3_base] ) ^ r1[ 69 - r1_base]

    temp1 = [t3]
    temp1.extend(r1[:-1])
    temp2 = [t1]
    temp2.extend(r2[:-1])
    temp3 = [t2]
    temp3.extend(r3[:-1])
    # print(len(temp1), " ", len(temp2)," ", len(temp3))
    return z, temp1, temp2, temp3

def genrate(key, iv):

    r1 = [ 0 for i in range(93)]
    r2 = [ 0 for i in range(84)]
    r3 = [ 0 for i in range(111)]

    r1, r2, r3 = loader(key, iv , r1, r2, r3)
    keyStream = ""
    for i in range(512):
        k, r1, r2, r3 = keyStreamGenerator(r1, r2, r3)
        keyStream+=str(k)
    print(keyStream)
    return format(int(keyStream, 2), "x")
    return keyStream







def handler():
    print("==============================[ Trivium Cipher ]==================   ")
    key = (input("Enter your  Key : "))
    iv = input("Enter your IV which you want to Encrypt : ")
    cipher = genrate(key, iv)
    print("Your KeyStream  is ")
    print("-----------------------------Chipher -----------------------")
    print(cipher)
    print("--------------------------------------------------------------")
    print(len(cipher))

handler()
