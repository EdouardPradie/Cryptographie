##
## EPITECH PROJECT, 2023
## crypto
## File description:
## rsa
##

from src.utils.Types import decimal_to_hexadecimal
from src.utils.Rsa import hexa_little_indian, pgcd
from src.utils.Arguments import IArgs

def generate_keys(public_key : str, private_key : str):
    p : int = int(hexa_little_indian(public_key), 16)
    q : int = int(hexa_little_indian(private_key), 16)
    n : int = p * q
    phi_n : int = (p - 1) * (q - 1)
    e : int = 256
    d : int = 0

    while (pgcd(e, phi_n) != 1 and e < phi_n):
        e += 1
    d = pow(e, -1, phi_n)
    print(f"public key: {(decimal_to_hexadecimal(e))}-{(decimal_to_hexadecimal(n))}")
    print(f"private key: {(decimal_to_hexadecimal(d))}-{(decimal_to_hexadecimal(n))}")

class Rsa():
    def __init__(self, data :IArgs):
        self.message = hexa_little_indian(data.message)
        tmp = data.key.split("-")
        self.key = hexa_little_indian(tmp[0])
        self.n = hexa_little_indian(tmp[1])
        self.result : str = ""

    def cipher(self):
        x : int = 0
        x = pow(int(self.message, 16), int(self.key, 16)) % int(self.n, 16)
        print(decimal_to_hexadecimal(x))

    def decipher(self):
        x : int = 0
        x = pow(int(self.message, 16), int(self.key, 16)) % int(self.n, 16)
        print(decimal_to_hexadecimal(x))
