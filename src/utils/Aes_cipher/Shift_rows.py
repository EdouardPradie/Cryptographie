##
## EPITECH PROJECT, 2023
## crypto
## File description:
## Aes_utils_shift_rows
##

def switch_box(row : list[str]):
    tmp : str = row[0]
    row = row[1:]
    row.append(tmp)
    return row

def shift_rows(matrix : list[list[str]]):
    tmp : list[list[str]] = [[], [], [], []]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            tmp[i].append(matrix[j][i])

    for i in range(len(tmp)):
        for j in range(i):
            tmp[i] = switch_box(tmp[i])

    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            matrix[i][j] = (tmp[j][i])
    return matrix