def inv_mix_column(matrixS):
    inv_mix_matrix = [
        [0x0e, 0x0b, 0x0d, 0x09],
        [0x09, 0x0e, 0x0b, 0x0d],
        [0x0d, 0x09, 0x0e, 0x0b],
        [0x0b, 0x0d, 0x09, 0x0e]
    ]

    result_matrix = []

    for i in range(4):
        col = []
        for j in range(4):
            val = 0
            for k in range(4):
                byte = int(matrixS[k][j], 16)
                inv_mix_val = inv_mix_matrix[i][k]

                if inv_mix_val == 0x09:
                    val ^= (byte << 1) ^ (0x1b if byte & 0x80 else 0x00) ^ byte
                elif inv_mix_val == 0x0b:
                    val ^= (byte << 1) ^ (0x1b if byte & 0x80 else 0x00) ^ byte
                elif inv_mix_val == 0x0d:
                    val ^= (byte << 1) ^ (0x1b if byte & 0x80 else 0x00) ^ byte
                elif inv_mix_val == 0x0e:
                    val ^= (byte << 1) ^ (0x1b if byte & 0x80 else 0x00)
            col.append(format(val & 0xFF, '02x'))
        result_matrix.append(col)

    return result_matrix

# Initial key
initial_key = [['66', '8d', '1c', 'd3'],
               ['83', 'd9', '68', '76'],
               ['af', '73', '77', 'a6'],
               ['80', '44', 'a4', 'e2']]

initial_key2 = [['66', '83', 'af', '80'],
               ['8d', 'd9', '73', '44'],
               ['1c', '68', '77', 'a4'],
               ['80', '76', 'a6', 'e2']]


initial_key = inv_mix_column(initial_key)
for key in initial_key:
    print(f"{key}")
print("")
initial_key2 = inv_mix_column(initial_key2)
for key in initial_key2:
    print(f"{key}")