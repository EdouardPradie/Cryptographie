##
## EPITECH PROJECT, 2023
## crypto
## File description:
## xor
##

from src.utils.Types import my_int, my_char
from src.utils.Arguments import IArgs

class Xor():
    def __init__(self, data :IArgs):
        if (len(data.message) != len(data.key)):
            raise ValueError("Message and key must be of the same size")
        self.message = data.message
        self.key =data.key
        self.result : str = [None] * len(data.message)

    def cipher(self):
        for i in range(len(self.message)):
            self.result[i] = my_char(my_int(self.message, i) ^ my_int(self.key, i))
        print("".join(self.result))

    def decipher(self):
        for i in range(len(self.message)):
            self.result[i] = my_char(my_int(self.message, i) ^ my_int(self.key, i))
        print("".join(self.result))
