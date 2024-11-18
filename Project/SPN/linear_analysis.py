import basic_SPN as cipher
import itertools as it
import collections
from math import fabs
from lat import lat

probBias = lat()
for row in probBias:
    print(' '.join([f'{(bia - 8):02d}' for bia in row]))

# Key analysis (focus on the last 16 bits of the key)
k = cipher.keyGeneration()
k_5 = int(k, 16) & 0xffff  # Last 16 bits of the key
k_5_5_8 = (k_5 >> 8) & 0b1111  # Bits 5 to 8 of K5
k_5_13_16 = k_5 & 0b1111  # Bits 13 to 16 of K5

# Print key and partial subkey information
print(f'\nTest key k = {k}')
print(f'(k_5 = {hex(k_5).zfill(4)})')
print(f'Target subkey K_5,5...k_5,8 = 0b{bin(k_5_5_8)[2:].zfill(4)} = 0x{hex(k_5_5_8)[2:].zfill(1)}')
print(f'Target subkey K_5,13...k_5,16 = 0b{bin(k_5_13_16)[2:].zfill(4)} = 0x{hex(k_5_13_16)[2:].zfill(1)}')

# Linear cryptanalysis: test each possible target subkey
countTargetBias = [0] * 256  # Count of matching approximations for each subkey value

# Test 10,000 random plaintexts
for pt in range(10000):
    ct = cipher.encrypt(pt, k)  # Encrypt plaintext with the key

    ct_5_8 = (ct >> 8) & 0b1111
    ct_13_16 = ct & 0b1111

    # Test each possible target subkey (0 to 255)
    for target in range(256):
        target_5_8 = (target >> 4) & 0b1111
        target_13_16 = target & 0b1111

        # Calculate the linear approximation
        v_5_8 = ct_5_8 ^ target_5_8
        v_13_16 = ct_13_16 ^ target_13_16

        u_5_8, u_13_16 = cipher.sbox_inv[v_5_8], cipher.sbox_inv[v_13_16]

        # Linear approximation equation
        lApprox = ((u_5_8 >> 2) & 0b1) ^ (u_5_8 & 0b1) ^ ((u_13_16 >> 2) & 0b1) ^ (u_13_16 & 0b1) \
                  ^ ((pt >> 11) & 0b1) ^ ((pt >> 9) & 0b1) ^ ((pt >> 8) & 0b1)

        # If approximation equals 0, it is a match
        if lApprox == 0:
            countTargetBias[target] += 1

# Calculate bias for each target subkey
bias = [fabs(count - 5000.0) / 10000.0 for count in countTargetBias]

# Find the subkey with the highest bias
maxResult, maxIdx = max((val, idx) for idx, val in enumerate(bias))

print(f'Highest bias is {maxResult} for subkey value {hex(maxIdx)}.')

# Check if the best match corresponds to the expected subkey
if (maxIdx >> 4) & 0b1111 == k_5_5_8 and maxIdx & 0b1111 == k_5_13_16:
    print('Success! The key was recovered.')
else:
    print('Failure. The key was not recovered.')
