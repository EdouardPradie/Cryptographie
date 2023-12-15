from src.utils.Aes_cipher.Sub_bytes import sbox

def add_front(string : str):
    string = string.replace("0x", "")
    if len(string) == 1:
        return "0" + string
    return string

def rotate(word):
    return word[1:] + word[:1]

def key_schedule_array(key):
    w = [int(key[i:i+2], 16) for i in range(0, len(key), 2)]
    key_array = [w[:4]]

    for i in range(4, 44):
        temp = w[(i-1) * 4:i * 4]

        if i % 4 == 0:
            temp = rotate(temp)
            temp = [int(sbox(add_front(hex(val))), 16) for val in temp]
            rcon = [i // 4, 0, 0, 0]
            temp = [temp[j] ^ rcon[j] for j in range(4)]

        new_word = [temp[j] ^ w[(i-4) * 4 + j] for j in range(4)]
        w.extend(new_word)
        if i % 4 == 0:
            key_array.append(w[i * 4:(i + 1) * 4])

    return [['{:02x}'.format(val) for val in sub_array] for sub_array in key_array]

# Initial key
initial_key = "6b50fd39f06d33cfefe6936430b6c94f"

# Generating key schedule in array form
key_schedule = key_schedule_array(initial_key)

# Displaying key schedule in array form
for i, key in enumerate(key_schedule):
    print(f"Round {i}: {key}")