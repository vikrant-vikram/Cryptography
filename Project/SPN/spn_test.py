import spn

defaultmsg = ('0010011010110111')
key = '101110001010101101110101011001000101101101'
cipher_text = spn.encrypt(defaultmsg, key)
print("Cipher Text: ", cipher_text)
# 25874
