# SSE (Searchable Symmetric Encryption)

## Final project for Fall'19 - 601.745 | Advanced topics in Cryptography

Trapdoor-based Searchable Symmetric Encryption Scheme for Data

In this project, we use trapdoor-based Searchable Symmetric Encryption scheme to run search queries on encrypted data. The input file used to test this implementation is a log file that tracks error reports and categories with over 4000 records.  

Implementation notes:

1. Generate a masterkey using masterkey_gen.  This creates a 16 byte long key which will be used to encrypt the input file and      generate a trapdoor for a keyword.

2. Build an Index using build_index.py:

   (a)input_index: The input file is encrypted using the masterkey and generates an index

   (b)Generate trapdoor: Uses masterkey and keyword as the input, and outputs the trapdoor of keyword.
   
   ![1final](https://user-images.githubusercontent.com/25291535/71326133-89a98680-24c4-11ea-9eb7-7c388df8e553.png)

   
   
3. sse_query.py: Used to search the encrypted input file for specific keywords that are saved as trapdoors.

   ![sq](https://user-images.githubusercontent.com/25291535/71326136-98903900-24c4-11ea-8d64-0bc66cbb1515.png)
