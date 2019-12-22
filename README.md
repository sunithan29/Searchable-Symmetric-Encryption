# SSE (Searchable Symmetric Encryption)

## Final project for Fall'19 - 601.745 | Advanced topics in Cryptography

Trapdoor-based Searchable Symmetric Encryption Scheme for Data

In this project, we use trapdoor-based Searchable Symmetric Encryption scheme to run search queries on encrypted data. The input file used to test this implementation is a log file that tracks error reports and categories with over 4000 records.  

Implementation notes:

1. Generate a masterkey using masterkey_gen.  This creates a 16 byte long key which will be used to encrypt the input file and      generate a trapdoor for a keyword. Ensure you choose the correct encoding and length for the key.
       
        $ python3 masterkey_gen.py > masterkey

2. Build an Index using build_index.py:
         
        $ python3 build_index.py
         
   (a)Phase I: input_index: The input file is encrypted using the masterkey and generates an index

   (b)Phase II: Generate trapdoor: Uses masterkey and keyword as the input, and outputs the trapdoor of keyword.
   
   ![1final](https://user-images.githubusercontent.com/25291535/71326133-89a98680-24c4-11ea-9eb7-7c388df8e553.png)

   
   
3. sse_query.py: Used to search the encrypted input file for specific keywords that are saved as trapdoors.

        $ python3 sse_query.py
       
   ![sq1](https://user-images.githubusercontent.com/25291535/71326459-1e15e800-24c9-11ea-80a3-5f2fabbc71b2.png)


