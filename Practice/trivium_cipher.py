


# # for 𝑖=1to𝑁
# #   do
#     # 𝑡1 ← 𝑠66 + 𝑠93
#     # 𝑡2 ← 𝑠162 + 𝑠177
#     # 𝑡3 ← 𝑠243 + 𝑠288
#     # 𝑧𝑖 ← 𝑡1 + 𝑡2 + 𝑡3
#     # 𝑡1 ←𝑡1 +𝑠91 ⋅𝑠92 +𝑠171
#     # 𝑡2 ←𝑡2 +𝑠175 ⋅𝑠176 +𝑠264
#     # 𝑡3 ←𝑡3 +𝑠286 ⋅𝑠287 + 𝑠69
#     # (𝑠1,𝑠2,...,𝑠93) ← (𝑡3,𝑠1,...,𝑠92)
#     # (𝑠94,𝑠95,...,𝑠177) ← (𝑡1,𝑠94,...,𝑠176)
#     # (𝑠178,𝑠179,...,𝑠288) ← (𝑡2,𝑠178,...,𝑠287)



# # The Trivium cryptography method has 288 bit states and uses three registers
# # (A, B and C), of 93, 84 and 111 bits. The method for each state is:
#     #
# # Contannt Field


decimal_to_hex = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}




r1_base = 1
r2_base = 94
r3_base = 178
r1_cap = 93
r2_cap = 84
r3_cap = 111
#Registers



def converter(val):
    print(val)
    ans = ""
    for i in range(0,int(len(val)/4)):
        temp = val[i*4: (i+1)*4]
        temp = temp[::-1]
        # print(temp)
        temp = int(temp, 2)
        ans+=decimal_to_hex[temp]
    return ans



def hexToBin(hex_string, reg):
    integer_value = int(hex_string, 16)
    binary_string = format(integer_value, f'0{reg}b')
    return binary_string[::-1]

def loader(key, IV, r1, r2, r3):
    bin_key = str(hexToBin(key, 80))
    bin_iv = str(hexToBin(IV, 80))
    # print(bin_key, " ", bin_iv)

    # bin_key = bin_key[::-1]
    # bin_iv = bin_iv[::-1]
    # print(bin_key, " ", bin_iv)


    counter = 0
    for k in bin_key:
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

    print(''.join(str(x) for x in r1), ''.join(str(x) for x in r2), ''.join(str(x) for x in r3))
    return r1, r2, r3



def xnor(a, b):
    return a&b


def keyStreamGenerator(r1, r2,  r3):

    t1 = r1[66 - r1_base] ^ r1[ 93 - r1_base]
    t2 = r2[ 162 - r2_base] ^ r2[ 177 - r2_base]
    t3 = r3[ 243 - r3_base]  ^ r3[ 288 - r3_base]

    z = t1 ^ t2 ^ t3

    t1 = t1 ^ xnor(r1[ 91 - r1_base], r1[ 92 - r1_base]) ^ r2 [171 - r2_base]
    t2 = t2 ^ xnor(r2[175 - r2_base],r2[176 - r2_base] ) ^ r3[264 - r3_base]
    t3 = t3 ^ xnor( r3[286 - r3_base],r3[287 - r3_base] ) ^ r1[ 69 - r1_base]

    temp1 = [t3]
    temp1.extend(r1[:-1])
    temp2 = [t1]
    temp2.extend(r2[:-1])
    temp3 = [t2]
    temp3.extend(r3[:-1])
    return z, temp1, temp2, temp3

def genrate(key, iv):
    r1 = [ 0 for i in range(93)]
    r2 = [ 0 for i in range(84)]
    r3 = [ 0 for i in range(111)]
    r1, r2, r3 = loader(key, iv , r1, r2, r3)
    keyStream = ""
    for i in range(4*288) :
        k, r1, r2, r3 = keyStreamGenerator(r1, r2, r3)

    for i in range(512):
        k, r1, r2, r3 = keyStreamGenerator(r1, r2, r3)
        keyStream+=str(k)


    return converter(keyStream)
    # return keyStream



def bigIndianLittleIndianConverter(data):
    ans = data[1]+data[0]+ data[3]+ data[2]
    return ans[::-1]






def handler():
    print("==============================[ Trivium Cipher ]==================   ")
    key = (input("Enter your  Key : "))
    iv = input("Enter your IV : ")
    cipher = genrate(key, iv)
    print("Your KeyStream  is ")
    print("-----------------------------[ Trivium KeyStream ]-----------------------")
    for i in range(0, len(cipher), 32):
        for j in range(0, 8):
            temp = cipher[4*j+i: 4*(j+1)+i].upper()[::-1]
            temp = bigIndianLittleIndianConverter(temp)
            print(temp, end=" ")
        print()
    print("------------------------------------------------------------------------")
    # print(len(cipher))

handler()


# def hex_to_bin(hex_string, length):
#     return format(int(hex_string.replace(" ", ""), 16), f'0{length}b')

# def generate_keystream(key, iv):
#     # Initialize state
#     state = [0] * 288
#     state[:80] = [int(b) for b in hex_to_bin(key, 80)]
#     state[93:173] = [int(b) for b in hex_to_bin(iv, 80)]
#     state[285] = state[286] = state[287] = 1

#     # Warm-up phase
#     for _ in range(4 * 288):
#         t1 = state[65] ^ state[92]
#         t2 = state[161] ^ state[176]
#         t3 = state[242] ^ state[287]

#         z = t1 ^ t2 ^ t3

#         t1 ^= (state[90] & state[91]) ^ state[170]
#         t2 ^= (state[174] & state[175]) ^ state[263]
#         t3 ^= (state[285] & state[286]) ^ state[68]

#         state = [t3] + state[:287]
#         state[92] = t1
#         state[176] = t2

#     # Generate keystream
#     keystream = ""
#     for _ in range(512):
#         t1 = state[65] ^ state[92]
#         t2 = state[161] ^ state[176]
#         t3 = state[242] ^ state[287]

#         z = t1 ^ t2 ^ t3

#         keystream += str(z)

#         t1 ^= (state[90] & state[91]) ^ state[170]
#         t2 ^= (state[174] & state[175]) ^ state[263]
#         t3 ^= (state[285] & state[286]) ^ state[68]

#         state = [t3] + state[:287]
#         state[92] = t1
#         state[176] = t2

#     return hex(int(keystream, 2))[2:].zfill(128).upper()

# # Test vectors
# key1 = "0000 0000 0000 0000 0000"
# iv1 = "0000 0000 0000 0000 0000"
# print(f"Key = {key1}\nIV = {iv1}")
# print(f"Keystream = {generate_keystream(key1, iv1)}")

# key2 = "8000 0000 0000 0000 0000"
# iv2 = "0000 0000 0000 0000 0000"
# print(f"\nKey = {key2}\nIV = {iv2}")
# print(f"Keystream = {generate_keystream(key2, iv2)}")
