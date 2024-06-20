""" This is an decoding-encoding algorithm known as CEASER-CIPHER """

import os

os.system("cls")

class CaeserCipher:
    """
    Interval between the encrypted and decrypted message is of 3 letters
    """

    def __init__(self,space):
        """
        initialing the list for encrypted and decrypted message
        """
        encrypted = [None] * 26                             # temp array for encryption
        decrypted = [None] * 26                             # temp array for decryption

        for k in range(26):
            encrypted[k] = chr((k + space) % 26 + ord('A'))
            decrypted[k] = chr((k - space) % 26 + ord('A'))
        
        self._forward = ''.join(encrypted)                  # will store as string
        self._backward = ''.join(decrypted)                 # since fixed
    
    def encrypt(self, message):
        """
        Return string representation encrypted message
        """
        
        return self._transform(message,self._forward)
    
    def decrypt(self, message):
        """
        Return string representation decrypted message
        """
        return self._transform(message,self._backward)
    
    def _transform(self,original,code):
        """
        Utility to perform transformation based on given code string
        """
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')                      # index from 0 to 25
                msg[k] = code[j]                                # replace this character
        return ''.join(msg)

cipher = CaeserCipher(int(input("Enter the value of spaces between the encrypted and decrypted spaces: ")))

message = input("Enter the message: ")
coded = cipher.encrypt(message)
print(coded)
encrypt = cipher.decrypt(coded)
print(encrypt)