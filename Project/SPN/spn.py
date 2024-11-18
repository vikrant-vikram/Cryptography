import random
import spn_supplymentary as spn_supp
import basic_methods as bm


def key_generator(main_key:str):
    key = []
    for i in range(6):
        # print(4*i,(4*i)+16)
        key.append(main_key[4*i:(4*i)+16])
    return key
    # return  [ k[0:4],k[4:8], k[8:12], k[12:16], k[16:20] ]

#
def substitution(temp):
    # print("Substitute : ", temp)
    ans = ""
    for i in range(0, 16, 4):  # Iterate over the 4-bit chunks
        # Convert the 4-bit segment (temp[i:i+4]) to an integer
        a = int(temp[i:i+4], 2)

        # print(f"Substitute {temp[i:i+4]} -> {a} (decimal)")

        # Lookup the S-box value and convert it to binary, ensuring it's 4 bits long
        substituted_value = bin(int(spn_supp.sbox[a], 16))[2:].zfill(4)

        # Replace the 4-bit chunk in temp using string concatenation
        # print("substitured value : ", substituted_value)
        ans+=substituted_value

    return ans  # Return the modified temp as a string


def permutation(temp):
    perm = [temp[spn_supp.pbox[i]] for i in range(16)]
    return "".join(perm)

def key_mixing(temp,key):
    return bm.xor(temp,key)


def encrypt(msg:str, main_key):
    key = key_generator(main_key)
    # print(key)
    state = msg
    # print(int(state,2))

    t = [int(i,2) for i in key]
    # print(t)
    for i in range(3):
        # print("Level : ", i+1, end=" \t ")
        state = key_mixing(state,key[i])
        # print(int(state,2))
        state = substitution(state)
        # print(int(state,2))
        state = permutation(state)
        # print(int(state,2))

    state = key_mixing(state, key[4])
    state = substitution(state)
    state = key_mixing(state,key[5])

    return ''.join(state)
