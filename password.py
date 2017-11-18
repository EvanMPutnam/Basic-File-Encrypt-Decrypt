from Crypto.Cipher import AES
import base64
import hashlib
import sys


def encrypt(someKey, text):
    '''
    Given a master key and a text string to encode
    it encrypts the text using AES and master key
    :param someKey master key to encrypt with:
    :param text text to ecnrypt:
    :return encrypted text:
    '''
    secret = AES.new(someKey[:32])
    tagStr = (str(text) + (AES.block_size - len(str(text)) % AES.block_size)* "\0")
    cipher = base64.b64encode(secret.encrypt(tagStr))
    return cipher.decode('UTF-8')



def decrypt(someKey, text):
    '''
    Decrypts a string of text given the master key used
    to encrypt it in the first place.  Will otherwise error.
    :param someKey the master key used to originally encrypt:
    :param text the text to decrypt with master key:
    :return decrypted text:
    '''
    secretDec = AES.new(someKey)
    dec = (secretDec.decrypt(base64.b64decode(text)))
    dec = dec.decode('UTF-8').rstrip("\0")
    return dec

def encryptFile(file, masterPass):
    '''
    Given a file and a master password encrypts the file
    using the master password.
    :param file:
    :param masterPass:
    :return none:
    '''
    encFile = open(file, 'r')
    data = encFile.read()
    encFile.close()
    textEnc = encrypt(masterPass, data)
    f = open(file, 'w')
    f.write(textEnc)
    f.close()

def decryptFile(file, masterPass):
    '''
    Given a file and a master password decrypts the file
    using the master password
    :param file the file that needs decrypting:
    :param masterPass the master password used to decrypt:
    :return decrypted text:
    '''
    decFile = open(file, 'r')
    data = decFile.read()
    decFile.close()
    data = decrypt(masterPass, data)
    return data





def main():
    '''
    Main function that handles command line arguments to
    command line encrypt/decrypt program
    :return:
    '''
    if(len(sys.argv) !=4):
        print("Usage: python password.py masterKey file [-d : decrypt, -e : encrypt]")
        print("Example: python password.py masterKey file.txt -d")
        return
    else:
        MASTER_PASS = sys.argv[1]
        MASTER_PASS = hashlib.sha256(MASTER_PASS.encode('utf-8')).digest()
        if(sys.argv[3] == "-e"):
            encryptFile(sys.argv[2], MASTER_PASS)
        elif(sys.argv[3] == "-d"):
            print(decryptFile(sys.argv[2], MASTER_PASS))
        else:
            print("Usage: python password.py masterKey file [-d : decrypt, -e : encrypt]")
            print("Example: python password.py masterKey file.txt -d")


if __name__ == '__main__':
    main()