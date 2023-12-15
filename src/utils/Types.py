##
## EPITECH PROJECT, 2023
## crypto
## File description:
## my_int
##

from src.utils.Rsa import hexa_little_indian

def decimal_to_hexadecimal(n : int):
    tmp : int = n
    hexadecimal = ""
    hexa_values = ["0", "1", "2", "3", "4", "5", "6", "7",
                   "8", "9", "a", "b", "c", "d", "e", "f"]
    if (n == 0):
        return "00"
    while tmp > 0:
        hexadecimal = hexa_values[tmp % 16] + hexadecimal
        tmp //= 16
    return hexa_little_indian(hexadecimal)

def my_int(char: str, idx: int):
    hexa_values = {"0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7,
                   "8" : 8, "9" : 9, "a" : 10, "b" : 11, "c" : 12, "d" : 13, "e" : 14, "f" : 15}
    return hexa_values[char[idx]]

def my_char(nb: int):
    if nb == 10:
        return 'a'
    if nb == 11:
        return 'b'
    if nb == 12:
        return 'c'
    if nb == 13:
        return 'd'
    if nb == 14:
        return 'e'
    if nb == 15:
        return 'f'
    return str(nb)