##
## EPITECH PROJECT, 2023
## crypto
## File description:
## rsa
##

##
## EPITECH PROJECT, 2023
## crypto
## File description:
## xor
##

from src.utils.Arguments import IArgs
from src.utils.Aes_cipher.Aes import big_indian, get_matrix_from_string, reverse
from src.utils.Aes_cipher.Mix_columns import mix_columns
from src.utils.Aes_cipher.Sub_bytes import sub_bytes
from src.utils.Aes_cipher.Shift_rows import shift_rows
from src.utils.Aes_cipher.Add_roundkey import get_new_matrix_key, add_roundkey
from src.utils.Aes_decipher.Shift_rows import shift_rows_des
from src.utils.Aes_decipher.Sub_bytes import sub_bytes_des
from src.utils.Aes_decipher.Mix_columns import mix_columns_des

RCON : list[list[str]] = [
  ["01" ,"00" ,"00" ,"00"],
  ["02" ,"00" ,"00" ,"00"],
  ["04" ,"00" ,"00" ,"00"],
  ["08" ,"00" ,"00" ,"00"],
  ["10" ,"00" ,"00" ,"00"],
  ["20" ,"00" ,"00" ,"00"],
  ["40" ,"00" ,"00" ,"00"],
  ["80" ,"00" ,"00" ,"00"],
  ["1b" ,"00" ,"00" ,"00"],
  ["36" ,"00" ,"00" ,"00"]
]

def get_keys(key: list[list[str]]) -> list[list[list[str]]]:
    all_keys : list[list[list[str]]] = []
    idx_key : int = 0

    for i in range(4):
        for j in range(4):
            key[i][j] = big_indian(key[i][j])
    all_keys.append(key)
    for rc in RCON:
            if len(all_keys) == 0:
                all_keys.append(get_new_matrix_key(key, rc))
            else:
                all_keys.append(get_new_matrix_key(all_keys[idx_key], rc))
            idx_key += 1
    return all_keys

def print_matrix(matrix : list[list[str]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="")
        print(" ", end="")
    print("\n")

def reverse_matrix(matrix : list[list[str]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = reverse(matrix[i][j])
    return matrix

def rev(liste : list[str]) -> list[str]:
    tmp : list[str] = []
    for i in range(len(liste)-1, -1, -1):
        tmp.append((liste[i]))
    return tmp

def get_key_round(all_keys : list[list[list[str]]], idx_key : int) -> list[list[str]]:
    result : list[list[str]] = []

    for i in range(len(all_keys[idx_key])):
        result.append([])
        for j in range(len(all_keys[idx_key][i])):
            result[i].append(reverse(all_keys[idx_key][i][j]))
    return result

class Aes():
    def __init__(self, data :IArgs):
        self.message : list[list[str]] = get_matrix_from_string(data.message)
        self.key : list[list[str]] = get_matrix_from_string(data.key)
        self.result : str = ""
        self.all_keys : list[list[list[str]]] = []
        self.idx_key : int = 0

    def cipher(self):
        self.all_keys = get_keys(self.key)
        self.message = add_roundkey(self.message, get_key_round(self.all_keys, self.idx_key))
        for i in range(9):
            self.message = sub_bytes(self.message)
            self.message = shift_rows(self.message)
            self.message = mix_columns(self.message)
            self.idx_key += 1
            self.message = add_roundkey(reverse_matrix(self.message), get_key_round(self.all_keys, self.idx_key))
        self.message = sub_bytes(self.message)
        self.message = shift_rows(self.message)
        self.idx_key += 1
        self.message = add_roundkey(reverse_matrix(self.message), get_key_round(self.all_keys, self.idx_key))
        for i in range(len(self.message)):
            for j in range(len(self.message[i])):
                self.result += self.message[i][j]
        print((self.result))

    def decipher(self):
        self.all_keys = rev(get_keys(self.key))
        self.message = add_roundkey(self.message, get_key_round(self.all_keys, self.idx_key))
        for i in range(9):
            self.message = shift_rows_des(self.message)
            self.message = sub_bytes_des(self.message)
            self.idx_key += 1
            self.message = add_roundkey(reverse_matrix(self.message), get_key_round(self.all_keys, self.idx_key))
            self.message = mix_columns_des(self.message)
        self.message = sub_bytes_des(self.message)
        self.message = shift_rows_des(self.message)
        self.idx_key += 1
        self.message = add_roundkey(reverse_matrix(self.message), get_key_round(self.all_keys, self.idx_key))
        for i in range(len(self.message)):
            for j in range(len(self.message[i])):
                self.result += self.message[i][j]
        print((self.result))
