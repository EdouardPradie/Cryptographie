##
## EPITECH PROJECT, 2023
## crypto
## File description:
## Aes_utils_mix_columns
##

from src.utils.Aes_cipher.Mix_columns import get_col


def inv_mix_columns(my_matrix : list[list[str]]):
    inv_mix_matrix = [
        ["0e", "0b", "0d", "09"],
        ["09", "0e", "0b", "0d"],
        ["0d", "09", "0e", "0b"],
        ["0b", "0d", "09", "0e"]
    ]
    result_matrix : list[list[str]] = [[], [], [], []]

    for i in range(4):
        result_matrix[i] = get_col(my_matrix[i], inv_mix_matrix)
    return result_matrix

def mix_columns_des(my_matrix : list[list[str]]):

    result = inv_mix_columns(my_matrix)
    return result
