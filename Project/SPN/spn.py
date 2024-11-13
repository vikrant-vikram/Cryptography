import random
import spn_supplymentary as spn_supp


def random_4bit_string()-> str:
    temp = ''.join(random.choice('01') for _ in range(16))
    print("key:",temp)
    return temp



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
    return perm

def key_mixing(temp):
    k = random_4bit_string()
    return ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(k, temp))


def spn(msg):

    state = msg
    for i in range(3):
        print("Level : ", i+1, end=" \t ")
        state = key_mixing(state)
        state = substitution(state)
        state = permutation(state)
    state = key_mixing(state)
    state = substitution(state)
    state = key_mixing(state)

    return ''.join(state)
