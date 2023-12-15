##
## EPITECH PROJECT, 2023
## crypto
## File description:
## Aes_utils
##

def reverse(string : str) -> str:
    tmp : str = ""
    tmp += string[1]
    tmp += string[0]
    return tmp

def big_indian(string : str):
    i : int = 0
    result : str = ""

    string = string.replace("0x", "")
    if (len(string) % 2 == 1):
        string = "0" + string
    while (i < len(string)):
        result += string[i + 1]
        result += string[i]
        i += 2
    return result

def get_matrix_from_string(string : str):
    matrix : list(list(str)) = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
    i : int = 0
    idx_i : int = 0
    idx_x : int = 0
    idx_y : int = 0

    string = big_indian(string)
    while (i < len(string)):
        matrix[idx_y][idx_x] += string[i]
        idx_i += 1
        if (idx_i == 2):
            idx_i = 0
            idx_x += 1
        if (idx_x == 4):
            idx_x = 0
            idx_y += 1
        if (idx_y == 4):
            break
        i += 1
    return matrix
