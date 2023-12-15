##
## EPITECH PROJECT, 2023
## crypto
## File description:
## Aes_utils_mix_columns
##

def galois_mul(a: int, b: int):
    p = 0
    for c in range(8):
        if b & 1:
            p ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11b
        b >>= 1
    return p

def get_col(matrix_col : list[str], mix : list[list[str]]):
    tmp : list[str] = ["" , "", "", ""]
    tmp[0] = format(galois_mul(int(mix[0][0], 16), int(matrix_col[0], 16)) ^ galois_mul(int(mix[0][1], 16), int(matrix_col[1], 16)) ^ galois_mul(int(mix[0][2], 16), int(matrix_col[2], 16)) ^ galois_mul(int(mix[0][3], 16), int(matrix_col[3], 16)), '02x')
    tmp[1] = format(galois_mul(int(mix[1][0], 16), int(matrix_col[0], 16)) ^ galois_mul(int(mix[1][1], 16), int(matrix_col[1], 16)) ^ galois_mul(int(mix[1][2], 16), int(matrix_col[2], 16)) ^ galois_mul(int(mix[1][3], 16), int(matrix_col[3], 16)), '02x')
    tmp[2] = format(galois_mul(int(mix[2][0], 16), int(matrix_col[0], 16)) ^ galois_mul(int(mix[2][1], 16), int(matrix_col[1], 16)) ^ galois_mul(int(mix[2][2], 16), int(matrix_col[2], 16)) ^ galois_mul(int(mix[2][3], 16), int(matrix_col[3], 16)), '02x')
    tmp[3] = format(galois_mul(int(mix[3][0], 16), int(matrix_col[0], 16)) ^ galois_mul(int(mix[3][1], 16), int(matrix_col[1], 16)) ^ galois_mul(int(mix[3][2], 16), int(matrix_col[2], 16)) ^ galois_mul(int(mix[3][3], 16), int(matrix_col[3], 16)), '02x')
    return tmp

def mix_columns(my_matrix : list[list[str]]):
    mix_matrix = [
        ["02", "03", "01", "01"],
        ["01", "02", "03", "01"],
        ["01", "01", "02", "03"],
        ["03", "01", "01", "02"]
    ]
    result_matrix : list[list[str]] = [[], [], [], []]

    for i in range(4):
        result_matrix[i] = get_col(my_matrix[i], mix_matrix)
    return result_matrix
