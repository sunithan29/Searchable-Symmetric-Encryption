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
    # start_time = time.time()
    for row in range(data_index.shape[0]):
        if gen_codeword(row, trapdoor) in data_index[row]:
            result.append(row)

    # print time.time() - start_time
    return result

if __name__ == "__main__":

  
    index_file_name = input("\nPlease input the index file you want to search:  ")
    keyword_trapdoor_file = input("\nPlease input the file where trapdoor is stored:  ")
    result_keyword_trapdoor = open(keyword_trapdoor_file, "wb")
    print (search_index(index_file_name, result_keyword_trapdoor))
