#########
#   
#   sse_query.py
#   
#   Used to search the encrypted input file for 
#   specific keywords that are saved as trapdoors.
#   This prints the list of all identifiers
#   for the keyword that is searched for.
#
#
#########

import pandas as pd
from Crypto.Cipher import AES
from Crypto.Hash import MD5
import hashlib
# import time

def gen_codeword(ID, trapdoor):
    
    # build a codeword using ID and the trapdoor function

    i = hashlib.md5()
    i.update(str(ID).encode())
    c = AES.new(trapdoor, AES.MODE_ECB)
    return c.encrypt(i.digest())

def search_index(document, trapdoor):
    result = [0]
    data_index = pd.read_csv(document)
    data_index = data_index.values
   
    for row in range(data_index.shape[0]):
        if gen_codeword(row, trapdoor) in data_index[row]:
            result.append(row)
 
    return result

if __name__ == "__main__":
    
    # Takes the input as the encrypted file 
    # and the trapdoor file. List all the 
    # identifiers that the keyword was found
    
    index_file_name = input("\nPlease input the index file you want to search:  ")
    keyword_trapdoor_file = input("\nPlease input the file where trapdoor is stored:  ")
    result_keyword_trapdoor = open(keyword_trapdoor_file, "wb")
    print (search_index(index_file_name, result_keyword_trapdoor))
