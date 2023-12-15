##
## EPITECH PROJECT, 2023
## crypto
## File description:
## Rsa_utils
##

def pgcd(a: int, b: int):
    while b:
        a, b = b, a % b
    return a

def hexa_little_indian(hexa : str):
    result : str = ""
    hexa = hexa.replace("0x", "")
    if (len(hexa) % 2 == 1):
        hexa = "0" + hexa
    for i in range(len(hexa) - 1, -1, -2):
        result += hexa[i - 1] + hexa[i]
    return result