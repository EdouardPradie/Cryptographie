##
## EPITECH PROJECT, 2023
## crypto
## File description:
## Aes_utils_add_roundkey
##

from src.utils.Aes_cipher.Aes import big_indian
from src.utils.Aes_cipher.Sub_bytes import sbox
from src.utils.Aes_cipher.Sub_bytes import sbox

def add_front(string : str):
    string = string.replace("0x", "")
    if len(string) == 1:
        return "0" + string
    return string

def rotate(word):
    return word[1:] + word[:1]

def get_new_matrix_key(matrix : list[list[str]], rcon : list[str]):
    new_matrix : list[list[str]] = []
    tmp : list[str] = ["", "", "", ""]

    for idx in range(len(matrix)):
        new_matrix.append([])
        if idx % 4 == 0:
            tmp = matrix[3]
            tmp = rotate(tmp)
            for i in range(len(tmp)):
                tmp[i] = sbox(tmp[i])
            for i in range(4):
                new_matrix[idx].append((add_front(hex(int(rcon[i], 16) ^ int(tmp[i], 16) ^ int(matrix[idx][i], 16)))))
        else:
            for i in range(4):
                new_matrix[idx].append((add_front(hex(int(new_matrix[idx - 1][i], 16) ^ int(matrix[idx][i], 16)))))
    return new_matrix

def add_roundkey(matrix_message : list[list[str]], matrix_key : list[list[str]]):
    for i in range(len(matrix_message)):
        for j in range(len(matrix_message[i])):
            matrix_message[i][j] = big_indian(hex(int(matrix_message[i][j], 16) ^ int(matrix_key[i][j], 16)))
    return matrix_message
