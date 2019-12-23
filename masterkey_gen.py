import os
import binascii

out = os.urandom(16)
print (binascii.hexlify(out))
