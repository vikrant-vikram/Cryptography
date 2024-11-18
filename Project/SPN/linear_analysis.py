# import spn as cipher
# import itertools as it
# import collections
# from math import fabs
# from lat import lat
# import basic_methods as bm


# from spn_supplymentary import sbox_inv
# probBias = lat()
# for row in probBias:
#     print(' '.join([f'{(bia - 8):02d}' for bia in row]))





# defaultmsg = list('0010011010110111')
# # key = '101110001010101101110101011001000101101101'

# # key = "000000000000000000000000000001000000"
# # k = cipher.key_generator(key)  # Assuming key_generator outputs a list of subkeys
# key = bm.random_36bit_string()
# # Key analysis (focus on the last 16 bits of the key)
# k = cipher.key_generator(key)
# k_5 = k[-1] # Last 16 bits of the key
# k_5_5_8 = k_5[4:8]  # Bits 5 to 8 of K5
# k_5_13_16 = k_5[12:16]  # Bits 13 to 16 of K5

# print(f'\nTest key k = {k}')
# print(f'(k_5 = {k_5})')
# print(f'Target subkey K_5,5...k_5,8 = {k_5_5_8}')
# print(f'Target subkey K_5,13...k_5,16 ={k_5_13_16}')

# # Linear cryptanalysis: test each possible target subkey
# countTargetBias = [0] * 256  # Count of matching approximations for each subkey value

# # Test 10,000 random plaintexts
# for pt in range(10000):
#     temp = bm.int_to_16bit_binary(pt)
#     ct = cipher.encrypt(temp, key)  # Encrypt plaintext with the key

#     ct_5_8 = ct[4:8]
#     ct_13_16 = ct[12:16]

#     # Test each possible target subkey (0 to 255)
#     for target in range(256):
#         temp = bm.int_to_16bit_binary(target)
#         target_5_8 = temp[4:8]
#         target_13_16 = temp[12:16]

#         # Calculate the linear approximation
#         # v_5_8 = ct_5_8 ^ target_5_8
#         v_5_8 = bm.xor(ct_5_8 , target_5_8)
#         # v_13_16 = ct_13_16 ^ target_13_16
#         v_13_16 = bm.xor(ct_13_16 , target_13_16)
#         # print(int(v_5_8, 2) , int(v_13_16, 2))
#         u_5_8, u_13_16 = sbox_inv[int(v_5_8, 2)], sbox_inv[int(v_13_16, 2)]

#         # Linear approximation equation
#         lApprox = ((u_5_8 >> 2) & 0b1) ^ (u_5_8 & 0b1) ^ ((u_13_16 >> 2) & 0b1) ^ (u_13_16 & 0b1) \
#                   ^ ((pt >> 11) & 0b1) ^ ((pt >> 9) & 0b1) ^ ((pt >> 8) & 0b1)

#         # If approximation equals 0, it is a match
#         if lApprox == 0:
#             countTargetBias[target] += 1

# # Calculate bias for each target subkey
# bias = [fabs(count - 5000.0) / 10000.0 for count in countTargetBias]

# # Find the subkey with the highest bias
# maxResult, maxIdx = max((val, idx) for idx, val in enumerate(bias))

# print(f'Highest bias is {maxResult} for subkey value {hex(maxIdx)}.')

# # Check if the best match corresponds to the expected subkey
# if (maxIdx >> 4) & 0b1111 == k_5_5_8 and maxIdx & 0b1111 == k_5_13_16:
#     print('Success! The key was recovered.')
# else:
#     print('Failure. The key was not recovered.')


import spn as cipher
import itertools as it
import collections
from math import fabs
from lat import lat
import basic_methods as bm
from spn_supplymentary import sbox_inv

# Linear Approximation Table (LAT) bias
probBias = lat()
for row in probBias:
    print(' '.join([f'{(bia - 8):02d}' for bia in row]))

# Default message and key (adjusted to 36 bits for now)
defaultmsg = list('0010011010110111')  # 16-bit binary message
key = bm.random_36bit_string()  # 36-bit key
# Key analysis (focus on the last 16 bits of the key)
k = cipher.key_generator(key)  # Assuming key_generator outputs a list of subkeys

# Last 16 bits (assuming k is already 16 bits long)
k_5 = k[-1]  # Last 16 bits of the key
k_5_5_8 = k_5[4:8]  # Bits 5 to 8 of K5
k_5_13_16 = k_5[12:16]  # Bits 13 to 16 of K5
print(f'\nkey = {key}')
print(f'\nTest key k = {k}')
print(f'(k_5 = {k_5})')
print(f'Target subkey K_5,5...k_5,8 = {k_5_5_8}')
print(f'Target subkey K_5,13...k_5,16 = {k_5_13_16}')

# Linear cryptanalysis: test each possible target subkey
countTargetBias = [0] * 256  # Count of matching approximations for each subkey value


# Test 10,000 random plaintexts
for pt in range(10000):
    temp = bm.int_to_16bit_binary(pt)  # Convert pt to 16-bit binary string
    ct = cipher.encrypt(temp, key)  # Encrypt plaintext with the key

    # Extract relevant bits from ciphertext
    ct_5_8 = ct[4:8]
    ct_13_16 = ct[12:16]

    # Test each possible target subkey (0 to 255)
    for target in range(256):
        target_bin = bm.int_to_8bit_binary(target)
        target_5_8 = target_bin[0:4]
        target_13_16 = target_bin[4:8]

        # XOR operation between ciphertext and target subkey bits
        v_5_8 = bm.xor(ct_5_8, target_5_8)
        v_13_16 = bm.xor(ct_13_16, target_13_16)

        u_5_8, u_13_16 = sbox_inv[int(v_5_8, 2)], sbox_inv[int(v_13_16, 2)]
        # print(u_5_8, u_13_16)
        # Linear approximation equation
        # lApprox = ((u_5_8 >> 2) & 0b1) ^ (u_5_8 & 0b1) ^ ((u_13_16 >> 2) & 0b1) ^ (u_13_16 & 0b1) \
        #           ^ ((pt >> 11) & 0b1) ^ ((pt >> 9) & 0b1) ^ ((pt >> 8) & 0b1)

        lApprox = int(u_5_8[1]) + int(u_5_8[-1]) + int(u_13_16[1]) + int(u_13_16[-1]) + int(temp[4]) + int(temp[6]) + int(temp[7])


        # If approximation equals 0, it is a match
        if (lApprox%2== 0):
            # print("dddd")
            countTargetBias[target] += 1

# Calculate bias for each target subkey
bias = [fabs(count - 5000.0) / 10000.0 for count in countTargetBias]

# Find the subkey with the highest bias
print(bias)
maxResult, maxIdx = max((val, idx) for idx, val in enumerate(bias))
temp = bm.int_to_8bit_binary(maxIdx)
print(temp)
print(f'Highest bias is {maxResult} for subkey value {hex(maxIdx)}.')

# Check if the best match corresponds to the expected subkey
if (maxIdx >> 4) & 0b1111 == k_5_5_8 and maxIdx & 0b1111 == k_5_13_16:
    print('Success! The key was recovered.')
else:
    print('Failure. The key was not recovered.')
