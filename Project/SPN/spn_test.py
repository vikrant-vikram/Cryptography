import spn

defaultmsg = list('0010011010110111')
key = '101110001010101101110101011001000101101101'
cipher_text = spn.spn(defaultmsg, key)
print("Cipher Text: ", cipher_text)
