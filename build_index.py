############
#
#  build_index.py
#
#  Serves as SSE implementation 
#  (a) Phase I: To build an index of the given input 
#      file and generate an encrypted file to search 
#      for keywords.
#  (b) Phase II: Generate a trapdoor for the keyword 
#      
############

import pandas as pd
import numpy as np
import hashlib
import time
import os
from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto.Random import random



def gen_trapdoor(MK, keyword):
    
    # build a trapdoor using the masterkey and keyword

    m = hashlib.md5()
    m.update(str(keyword).encode())
    iv = os.urandom(16)
    c = AES.new(MK, AES.MODE_CBC, iv)
    return (iv + c.encrypt(m.digest()))



def gen_codeword(ID, trapdoor):
    
    # build a codeword using ID and the trapdoor function
    
    i = hashlib.md5()
    i.update(str(ID).encode())
    iv = os.urandom(16)
    c = AES.new(trapdoor, AES.MODE_CBC, iv)
    return (iv + c.encrypt(i.digest()))


def build_index(MK, ID, keyword_list):
     
    # build index for the given input file

    secure_index = [0] * len(keyword_list)
    for item in range(len(keyword_list)):
        codeword = gen_codeword(ID, gen_trapdoor(MK, keyword_list[item]))
        secure_index[item] = codeword
    random.shuffle(secure_index)
    return secure_index

def searchable_encryption(raw_data_file_name, master_key, key_list):
    raw_data = pd.read_csv(raw_data_file_name)
    features = list(raw_data)
    raw_data = raw_data.values

    keyword_number = [i for i in range(0, len(features)) 
			if features[i] in keylist]

    index_header = []
    for i in range(1, len(keylist) + 1):
        index_header.append("index_" + str(i))

    document_index = []
    start_time = time.time()
    for row in range(raw_data.shape[0]):
        record = raw_data[row]
        record_keyword_list = [record[i] for i in keyword_number]
        record_index = build_index(master_key, row, record_keyword_list)
        document_index.append(record_index)

    time_cost = time.time() - start_time
    print ("\nThe time taken to generate the input_index.csv file is")
    print (time_cost)
    document_index_dataframe = pd.DataFrame(np.array(document_index), columns=index_header)
    document_index_dataframe.to_csv(raw_data_file_name.split(".")[0] + "_index.csv")

genFolder = "genResults"


if __name__ == "__main__":


# Phase I: 
# Building index
    
    # Use the master key to build index and generate trapdoor
    # This master key can be different for every query
    
    print ("\n\tPhase I: Building Index")
    master_key_file_name = input("\nPlease input the file/directory where the master key is stored:  ")
    master_key = open(master_key_file_name).read()
    
    # Check the lenghth of the key that was given
    # ensure it is atleast 16 bytes

    if len(master_key) > 16:
        print ("the length of master key is larger than 16 bytes, only the first 16 bytes are used")
        master_key = bytes(master_key[:16])
    print ("\nSuccessfully added master key.")
    print ("\nAn index file will be generated for the input file.")  

    # Lets the user input the file that must be encrypted

    document_name = input("\tPlease input the file to be encrypted:  ")  
    
    # Lets the user choose the list of keywords 
    # that will be used to query the encrypted input file

    keyword_list_file_name = input("\tplease input the file where the keywords are listed:  ")
    keylist = open(keyword_list_file_name).read().split(",")

    print (searchable_encryption(document_name, master_key, keylist))


# Phase II
# Genaration of Trapdoor for a keyword
  
    print ("\n\tPhase II: Trapdoor Generation for a keyword")
    
    # User can choose a keyword from the list of keywords
    # that will be used by the sse search

    keyword = input("\nPlease input the keyword you want to search for in the encrypted input file:  ")
    
    # Print and save the trapdoor generated 
    # for the keyword. This will be used by 
    # searchable_encryption.py

    trapdoor_file = open("keyword_trapdoor.csv", "wb")
    
    print ("\nA trapdoor for the keyword is successfully generated.") 
    print ("\tThe trapdoor is saved as keyword_trapdoor.csv file\n")
    print (gen_trapdoor(master_key, keyword)) 
    

    trapdoor_of_keyword = gen_trapdoor(master_key, keyword)
    trapdoor_file.write(trapdoor_of_keyword)
    trapdoor_file.close()
    
    print ("Finished")


   

