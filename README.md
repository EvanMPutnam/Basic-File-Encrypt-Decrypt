# Basic-File-Encrypt-Decrypt
A basic file encryption/decryption python command line tool.  Uses AES for encryption of text files.


# Encrypt
python password.py masterKey textFile.txt -e

# Decrypt
python password.py masterKey textFile.txt -d

# Notes
I have included a gui for ease of use.  You should never re-encrypt your text file as when you decrypt you will merely get the original encryption.  It is also worth noting that this is in python3 and needs cypto library installed.

You can install with the following

pip install crypto
  

