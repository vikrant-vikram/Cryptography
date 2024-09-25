
# ===================Data Encryption Standard (DES) block cipher.================================


# IP
# 58	50	42	34	26	18	10	2
# 60	52	44	36	28	20	12	4
# 62	54	46	38	30	22	14	6
# 64	56	48	40	32	24	16	8
# 57	49	41	33	25	17	9	1
# 59	51	43	35	27	19	11	3
# 61	53	45	37	29	21	13	5
# 63	55	47	39	31	23	15	7


# IP−1
# 40	8	48	16	56	24	64	32
# 39	7	47	15	55	23	63	31
# 38	6	46	14	54	22	62	30
# 37	5	45	13	53	21	61	29
# 36	4	44	12	52	20	60	28
# 35	3	43	11	51	19	59	27
# 34	2	42	10	50	18	58	26
# 33	1	41	9	49	17	57	25


# E
# 32	1	2	3	4	5
# 4	5	6	7	8	9
# 8	9	10	11	12	13
# 12	13	14	15	16	17
# 16	17	18	19	20	21
# 20	21	22	23	24	25
# 24	25	26	27	28	29
# 28	29	30	31	32	1


#
# S-boxes
# S1	x0000x	x0001x	x0010x	x0011x	x0100x	x0101x	x0110x	x0111x	x1000x	x1001x	x1010x	x1011x	x1100x	x1101x	x1110x	x1111x
# 0yyyy0	14	4	13	1	2	15	11	8	3	10	6	12	5	9	0	7
# 0yyyy1	0	15	7	4	14	2	13	1	10	6	12	11	9	5	3	8
# 1yyyy0	4	1	14	8	13	6	2	11	15	12	9	7	3	10	5	0
# 1yyyy1	15	12	8	2	4	9	1	7	5	11	3	14	10	0	6	13
# S2	x0000x	x0001x	x0010x	x0011x	x0100x	x0101x	x0110x	x0111x	x1000x	x1001x	x1010x	x1011x	x1100x	x1101x	x1110x	x1111x
# 0yyyy0	15	1	8	14	6	11	3	4	9	7	2	13	12	0	5	10
# 0yyyy1	3	13	4	7	15	2	8	14	12	0	1	10	6	9	11	5
# 1yyyy0	0	14	7	11	10	4	13	1	5	8	12	6	9	3	2	15
# 1yyyy1	13	8	10	1	3	15	4	2	11	6	7	12	0	5	14	9
# S3	x0000x	x0001x	x0010x	x0011x	x0100x	x0101x	x0110x	x0111x	x1000x	x1001x	x1010x	x1011x	x1100x	x1101x	x1110x	x1111x
# 0yyyy0	10	0	9	14	6	3	15	5	1	13	12	7	11	4	2	8
# 0yyyy1	13	7	0	9	3	4	6	10	2	8	5	14	12	11	15	1
# 1yyyy0	13	6	4	9	8	15	3	0	11	1	2	12	5	10	14	7
# 1yyyy1	1	10	13	0	6	9	8	7	4	15	14	3	11	5	2	12
# S4	x0000x	x0001x	x0010x	x0011x	x0100x	x0101x	x0110x	x0111x	x1000x	x1001x	x1010x	x1011x	x1100x	x1101x	x1110x	x1111x
# 0yyyy0	7	13	14	3	0	6	9	10	1	2	8	5	11	12	4	15
# 0yyyy1	13	8	11	5	6	15	0	3	4	7	2	12	1	10	14	9
# 1yyyy0	10	6	9	0	12	11	7	13	15	1	3	14	5	2	8	4
# 1yyyy1	3	15	0	6	10	1	13	8	9	4	5	11	12	7	2	14
# S5	x0000x	x0001x	x0010x	x0011x	x0100x	x0101x	x0110x	x0111x	x1000x	x1001x	x1010x	x1011x	x1100x	x1101x	x1110x	x1111x
# 0yyyy0	2	12	4	1	7	10	11	6	8	5	3	15	13	0	14	9
# 0yyyy1	14	11	2	12	4	7	13	1	5	0	15	10	3	9	8	6
# 1yyyy0	4	2	1	11	10	13	7	8	15	9	12	5	6	3	0	14
# 1yyyy1	11	8	12	7	1	14	2	13	6	15	0	9	10	4	5	3
# S6	x0000x	x0001x	x0010x	x0011x	x0100x	x0101x	x0110x	x0111x	x1000x	x1001x	x1010x	x1011x	x1100x	x1101x	x1110x	x1111x
# 0yyyy0	12	1	10	15	9	2	6	8	0	13	3	4	14	7	5	11
# 0yyyy1	10	15	4	2	7	12	9	5	6	1	13	14	0	11	3	8
# 1yyyy0	9	14	15	5	2	8	12	3	7	0	4	10	1	13	11	6
# 1yyyy1	4	3	2	12	9	5	15	10	11	14	1	7	6	0	8	13
# S7	x0000x	x0001x	x0010x	x0011x	x0100x	x0101x	x0110x	x0111x	x1000x	x1001x	x1010x	x1011x	x1100x	x1101x	x1110x	x1111x
# 0yyyy0	4	11	2	14	15	0	8	13	3	12	9	7	5	10	6	1
# 0yyyy1	13	0	11	7	4	9	1	10	14	3	5	12	2	15	8	6
# 1yyyy0	1	4	11	13	12	3	7	14	10	15	6	8	0	5	9	2
# 1yyyy1	6	11	13	8	1	4	10	7	9	5	0	15	14	2	3	12
# S8	x0000x	x0001x	x0010x	x0011x	x0100x	x0101x	x0110x	x0111x	x1000x	x1001x	x1010x	x1011x	x1100x	x1101x	x1110x	x1111x
# 0yyyy0	13	2	8	4	6	15	11	1	10	9	3	14	5	0	12	7
# 0yyyy1	1	15	13	8	10	3	7	4	12	5	6	11	0	14	9	2
# 1yyyy0	7	11	4	1	9	12	14	2	0	6	10	13	15	3	5	8
# 1yyyy1	2	1	14	7	4	10	8	13	15	12	9	0	3	5	6	11


# Parity Drop Table
# 1	2	3	4	5	6	7	8
# 9	10	11	12	13	14	15	16
# 17	18	19	20	21	22	23	24
# 25	26	27	28	29	30	31	32
# 33	34	35	36	37	38	39	40
# 41	42	43	44	45	46	47	48
# 49	50	51	52	53	54	55	56
# 57	58	59	60	61	62	63	64


# Permutation Table
# 1	2	3	4	5	6	7	8
# 0	57	49	41	33	25	17	9	1
# 1	58	50	42	34	26	18	10	2
# 2	59	51	43	35	27	19	11	3
# 3	60	52	44	36	63	55	47	39
# 4	31	23	15	7	62	54	46	38
# 5	30	22	14	6	61	53	45	37
# 6	29	21	13	5	28	20	12	4



# Bits Rotation Table
# Number of Round	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16
# Number of Left rotations	1	1	2	2	2	2	2	2	1	2	2	2	2	2	2	1



# # Key Compression Table
# 1	2	3	4	5	6	7	8
# 1	14	17	11	24	01	05	03	28
# 2	15	06	21	10	23	19	12	04
# 3	26	08	16	07	27	20	13	02
# 4	41	52	31	37	47	55	30	40
# 5	51	45	33	48	44	49	39	56
# 6	34	53	46	42	50	36	29	32



# ============================Statics ===========================
#


# from firstSem.CRYPTO.Assignment.trivium_cipher import converter



av = []

base = 1

IP = [  58, 50, 42, 34, 26,  18, 10, 2,
        60, 52, 44, 36,	28,	20,	12,	4,
        62,	54,	46,	38,	30,	22,	14,	6,
        64,	56,	48,	40,	32,	24,	16,	8,
        57,	49,	41,	33,	25,	17,	9,	1,
        59,	51,	43,	35,	27,	19,	11,	3,
        61,	53,	45,	37,	29,	21,	13,	5,
        63,	55,	47,	39,	31,	23,	15,	7
        ]


IP_1 = [40,	8,	48,	16,	56,	24,	64,	32,
        39,	7,	47,	15,	55,	23,	63,	31,
        38,	6,	46,	14,	54,	22,	62,	30,
        37,	5,	45,	13,	53,	21,	61,	29,
        36,	4,	44,	12,	52,	20,	60,	28,
        35,	3,	43,	11,	51,	19,	59,	27,
        34,	2,	42,	10,	50,	18,	58,	26,
        33,	1,	41,	9,	49,	17,	57,	25
        ]
E = [
        32, 1,	2,	3,	4,	5,
        4,	5,	6,	7,	8,	9,
        8,	9,	10,	11,	12,	13,
        12,	13,	14,	15,	16,	17,
        16,	17,	18,	19,	20,	21,
        20,	21,	22,	23,	24,	25,
        24,	25,	26,	27,	28,	29,
        28,	29,	30,	31,	32,	1
    ]



sbox = [
            [
                [14,	4,	13,	1,	2,	15,	11,	8,	3,	10,	6,	12,	5,	9,	0,	7],
                [0,	15,	7,	4,	14,	2,	13,	1,	10,	6,	12,	11,	9,	5,	3,	8],
                [4,	1,	14,	8,	13,	6,	2,	11,	15,	12,	9,	7,	3,	10,	5,	0],
                [15,	12,	8,	2,	4,	9,	1,	7,	5,	11,	3,	14,	10,	0,	6,	13]
            ],
            [
                [15,	1,	8,	14,	6,	11,	3,	4,	9,	7,	2,	13,	12,	0,	5,	10],
                [3,	13,	4,	7,	15,	2,	8,	14,	12,	0,	1,	10,	6,	9,	11,	5],
                [0,	14,	7,	11,	10,	4,	13,	1,	5,	8,	12,	6,	9,	3,	2,	15],
                [13,	8,	10,	1,	3,	15,	4,	2,	11,	6,	7,	12,	0,	5,	14,	9]
           	],
            [
                [10,	0,	9,	14,	6,	3,	15,	5,	1,	13,	12,	7,	11,	4,	2,	8],
                [13,	7,	0,	9,	3,	4,	6,	10,	2,	8,	5,	14,	12,	11,	15,	1],
                [13,	6,	4,	9,	8,	15,	3,	0,	11,	1,	2,	12,	5,	10,	14,	7],
                [1,	10,	13,	0,	6,	9,	8,	7,	4,	15,	14,	3,	11,	5,	2,	12]
            ],
            [

                [7,	13,	14,	3,	0,	6,	9,	10,	1,	2,	8,	5,	11,	12,	4,	15],
                [13,	8,	11,	5,	6,	15,	0,	3,	4,	7,	2,	12,	1,	10,	14,	9],
                [10,	6,	9,	0,	12,	11,	7,	13,	15,	1,	3,	14,	5,	2,	8,	4],
                [3,	15,	0,	6,	10,	1,	13,	8,	9,	4,	5,	11,	12,	7,	2,	14]
            ],
            [

                [2,	12,	4,	1,	7,	10,	11,	6,	8,	5,	3,	15,	13,	0,	14,	9],
                [14,	11,	2,	12,	4,	7,	13,	1,	5,	0,	15,	10,	3,	9,	8,	6 ],
                [4,	2,	1,	11,	10,	13,	7,	8,	15,	9,	12,	5,	6,	3,	0,	14],
                [11,	8,	12,	7,	1,	14,	2,	13,	6,	15,	0,	9,	10,	4,	5,	3]
            ],
            [

                [12,	1,	10,	15,	9,	2,	6,	8,	0,	13,	3,	4,	14,	7,	5,	11],
                [10,	15,	4,	2,	7,	12,	9,	5,	6,	1,	13,	14,	0,	11,	3,	8],
                [9,	14,	15,	5,	2,	8,	12,	3,	7,	0,	4,	10,	1,	13,	11,	6],
                [4,	3,	2,	12,	9,	5,	15,	10,	11,	14,	1,	7,	6,	0,	8,	13]
            ],
            [

                [4,	11,	2,	14,	15,	0,	8,	13,	3,	12,	9,	7,	5,	10,	6,	1],
                [13,	0,	11,	7,	4,	9,	1,	10,	14,	3,	5,	12,	2,	15,	8,	6],
                [1,	4,	11,	13,	12,	3,	7,	14,	10,	15,	6,	8,	0,	5,	9,	2],
                [6,	11,	13,	8,	1,	4,	10,	7,	9,	5,	0,	15,	14,	2,	3,	12]
           	],
            [
                [13,	2,	8,	4,	6,	15,	11,	1,	10,	9,	3,	14,	5,	0,	12,	7],
                [1,	15,	13,	8,	10,	3,	7,	4,	12,	5,	6,	11,	0,	14,	9,	2],
                [7,	11,	4,	1,	9,	12,	14,	2,	0,	6,	10,	13,	15,	3,	5,	8],
                [2,	1,	14,	7,	4,	10,	8,	13,	15,	12,	9,	0,	3,	5,	6,	11],
            ]
        ]





key_permutation_table = [
    57,	49,	41,	33,	25,	17,	9,	1,
    58,	50,	42,	34,	26,	18,	10,	2,
    59,	51,	43,	35,	27,	19,	11,	3,
    60, 52,	44,	36,	63,	55,	47,	39,
    31,	23,	15,	7, 62, 54,	46,	38,
    30,	22,	14,	6, 61,	53,	45,	37,
    29,	21,	13,	5, 28,	20,	12,	4
]





bits_Rotation_table = [1, 1, 2,	2, 2, 2, 2,	2,	1, 2,	2,	2,	2,	2,	2,	1]



key_compression_table = [

    14,	17,	11,	24,	1,	5,	3,	28,
    15,	6,	21,	10,	23,	19,	12,	4,
    26,	8,	16,	7,	27,	20,	13,	2,
    41,	52,	31,	37,	47,	55,	30,	40,
    51,	45,	33,	48,	44,	49,	39,	56,
    34,	53,	46,	42,	50,	36,	29,	32
]


per = [16, 7, 20, 21,
	29, 12, 28, 17,
	1, 15, 23, 26,
	5, 18, 31, 10,
	2, 8, 24, 14,
	32, 27, 3, 9,
	19, 13, 30, 6,
	22, 11, 4, 25]

decimal_to_hex = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}


int_to_bin = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
 '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

binary_to_hex = {
    '0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4',
    '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9',
    '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
}

hex_to_binary = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
    '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
    'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}


def converter_binary_to_hex( l :list[int])-> str:
    hex_string = ""
    for i in range(len(l)//4):
        bit = i*4
        binary_string = str(l[bit])+ str(l[bit + 1]) + str(l[bit + 2]) + str(l[bit + 3])
        # print(binary_string)
        hex_string+=binary_to_hex[binary_string]
    return hex_string



def rotate_left( l:list[int], times:int) -> list[int]:
    # return list(map(int,shift_left("".join(map(str,l)),times).split()))
    # print("".join(map(str,l)), times)
    temp = []
    for i in range(times):
        temp.extend(l[1:])
        temp.append(l[0])
        l = temp
        temp= []
    # print("".join(map(str,l)))
    return l

def key_copression(first_28_bits : list[int], last_28_bits:list[int]) -> list[int]:

    total = []
    compressed_key = []
    total.extend(first_28_bits)
    total.extend(last_28_bits)
    for i in key_compression_table:
        temp = i-1
        compressed_key.append(total[temp])
    return compressed_key



def keyGeneration(key: list[int]) -> list[list[int]]:
    list_of_key =[]
    counter = 0
    # 2.Priority Drop -> 64bit to 56 bit using Priority Drop Table
    after_drop_and_permutation = [0 for i in range(56)]
    for i in key_permutation_table:
        after_drop_and_permutation[counter] = key[i-1]
        counter+=1
    # 3. Devide 56 bits into 28 28 bits
    first_28_bits = after_drop_and_permutation[:28]
    last_28_bits = after_drop_and_permutation[28:]

    for round in range(16):
        # 4.Left Shift
        first_28_bits = rotate_left(first_28_bits, bits_Rotation_table[round] )
        last_28_bits = rotate_left(last_28_bits, bits_Rotation_table[round] )
        # 5. Compression of key 28+28 -> 48
        list_of_key.append(key_copression(first_28_bits, last_28_bits))
    return list_of_key



# Rerturn xor of two binary list as list
def xor(l1:list[int] , l2:list[int])-> list[int]:
    result = []
    for i in range(len(l1)):
        result.append(l1[i] ^ l2[i])
    return result


def permute(k, arr, n):
	permutation = ""
	for i in range(0, n):
		permutation = permutation + k[arr[i] - 1]
	return permutation


def des_round_function(r1 : list[int], round_key:list[int]) -> list[int]:
    expanded_r1 = []
    for i in E:
        temp = i-1
        expanded_r1.append(r1[temp])
    result_of_xor = xor(expanded_r1, round_key)
    # print("".join(list(map(str,result_of_xor))))


    # for i in range(48):
    #     result_of_xor.append(expanded_r1[i] ^ [i])

    binary_string = ""
    for i in range(8):
        # print(i*6, (i+1)*6)
        lookup = result_of_xor[i*6: (i+1)*6]

        # int('11111111', 2)
        # print(lookup)
        row = int(str(lookup[0])+ str(lookup[-1]), 2)
        col = int( str(lookup[1]) + str(lookup[2]) + str(lookup[3]) + str(lookup[4]), 2)

        val = sbox[i][row][col]
        # print(val)
        binary_string+=int_to_bin[val]
    sbox_str = permute(binary_string, per, 32)
    # print("binary_string",binary_string)

    return list(map(int, list(sbox_str)))



def DES(plainText:list[int] , key: list[int]):
    result1 = []
    encrypted_block = []
    # 1. Initial Permutation
    plain_text_after_permutation = []
    for i in IP:
        temp = i-1
        plain_text_after_permutation.append(plainText[temp])
    # 2 . Generate Round Keys
    round_keys = keyGeneration(key)
    # 3. Devide 64 bits into two 32 bit blocks
    l_first_32_bits = plain_text_after_permutation[:32]
    r_last_32_bits = plain_text_after_permutation[32:]
    print("After initial Permutation : " , converter_binary_to_hex(plain_text_after_permutation))
    print("After splitting: L0: ",converter_binary_to_hex(l_first_32_bits), "R0 : ",converter_binary_to_hex(r_last_32_bits ))
    print("Left                         Right                     Round Key")

    for i in range(16):
        # 4. Pass Right 32 bits and respective Round Keys
        result = des_round_function(r_last_32_bits, round_keys[i])

        temp = r_last_32_bits
        # 5. XOR the Result of DES round Function and First 32 bits
        # 6. Store the XOR result in R and R into L
        r_last_32_bits = xor(result, l_first_32_bits)
        l_first_32_bits = temp
        round_i_result = []
        if(i == 15):
            # print("Swap")
            l_first_32_bits , r_last_32_bits = r_last_32_bits, l_first_32_bits
        print("L"+str(i+1),": ", converter_binary_to_hex(l_first_32_bits),"\t\tR" + str(i+1), ": ", converter_binary_to_hex(r_last_32_bits), "\t\tKey : ", converter_binary_to_hex(round_keys[i]))

        round_i_result.extend(l_first_32_bits)
        round_i_result.extend(r_last_32_bits)
        result1.append(round_i_result)
    av.append(result1)
    # Do 4 5 and 6th Steps 16 times in total
    # cipherText.extend(l_first_32_bits)
    l_first_32_bits.extend(r_last_32_bits)
    total  = l_first_32_bits

    # print("Total len :" , len(total))
    # 7. On the result use Final Permutation
    for i in IP_1:
        # print(i)
        temp = i-1
        encrypted_block.append(total[temp])
    # 8. Return the Result
    return encrypted_block



# function converts each character of the input string to its 4-bit binary representation
def string_to_4bit_binary(input_string : str) -> list[int]:
    binary_list = []
    for char in input_string:
        binary_list.extend(list(map(int,list(hex_to_binary[char]))))
    return binary_list





#This function takes PlainText:Hexadecimal and Key:Hexadecimal then convert it into blocks and pass it to the DES
def encrypt(plaintext:str, key:str)->str:
    cipherText =""
    plaintext_binary = string_to_4bit_binary(plaintext)
    key_binary = string_to_4bit_binary(key)
    cipher_binary = []
    for i in range(len(plaintext_binary)//64):
        cipher_binary.extend(DES(plaintext_binary[i*64: (i+1)*64], key_binary))
    cipherText = converter_binary_to_hex(cipher_binary)
    # for bit in range(len(cipher_binary)//4):
    #     binary_string = str(cipher_binary[bit])+ str(cipher_binary[bit + 1]) + str(cipher_binary[bit + 2]) + str(cipher_binary[bit + 3])
    #     cipherText+=binary_to_hex[binary_string]
    return cipherText




def avalanche():
    plainText = input("Plaintext : ")
    key = input("Key : ")
    print("Cipher text : ",encrypt(plainText,key))

    plainText = input("Plaintext : ")
    key = input("Key : ")
    print("Cipher text : ",encrypt(plainText,key))

    first = av[0]
    second = av[1]
    print("Avalanche Property")
    print("Rounds     Bit differences")
    for i in range(len(first)):
        temp1 = first[i]
        temp2 = second[i]
        print( i+1 , "\t\t" , sum(xor(temp1, temp2)))



def handler():
    print("\033[93m"+"===========================[ Data Encryption Standard ]==============================")
    print("Input Should be in HEXA")
    print("\033[96m")
    print("Choose an option")
    print("1. DES Encryption")
    print("2. Avalanche Property")
    option = int(input())
    if(option == 1):
        plainText = input("Plaintext : ")
        key = input("Key : ")
        # plainText = "123456ABCD132536"
        # key = "AABB09182736CCDD"


        print("Cipher text : ",encrypt(plainText,key))

    elif(option == 2):
        avalanche()
    else:
        print("Choose Vailid Option")
handler()
