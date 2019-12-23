##########
#
#  masterkey_gen.py
#
#  This script generates a masterkey that is used for
#  the AES encryption scheme. Generate a new masterkey
#  for every keyword search for stronger security.
#
##########
import os
import binascii

out = os.urandom(16)
print (binascii.hexlify(out))
