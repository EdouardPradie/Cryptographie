##
## EPITECH PROJECT, 2023
## crypto
## File description:
## Aes_utils_shift_rows
##

def shift_rows_des(matrix : list[list[str]]):
    tmp : list[list[str]] = [[], [], [], []]

    for i in range(4):
        for j in range(4):
            tmp[j].append(matrix[(i - j) % 4][j])
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            matrix[i][j] = (tmp[j][i])
    return matrix