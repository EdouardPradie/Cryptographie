##
## EPITECH PROJECT, 2023
## crypto
## File description:
## Crypto
##

from src.Cryptos.Rsa import generate_keys, Rsa
from src.Cryptos.Xor import Xor
from src.Cryptos.Aes import Aes
from src.utils.Arguments import IArgs

def crypto_exe(args: IArgs):
    if (args.crypto == "xor"):
        args.message : str | None = input()
        if (args.message == None):
            raise ValueError("no message input")
        xor = Xor(args)
        if (args.mode == "cipher"):
            xor.cipher()
            return 0
        if (args.mode == "decipher"):
            xor.decipher()
            return 0
        raise ValueError("Invalid mode")

    if (args.crypto == "rsa"):
        if (args.mode == "generate"):
            generate_keys(args.public_key, args.private_key)
            return 0
        args.message : str | None = input()
        rsa = Rsa(args)
        if (args.mode == "cipher"):
            rsa.cipher()
            return 0
        if (args.mode == "decipher"):
            rsa.decipher()
            return 0
        raise ValueError("Invalid mode")

    if (args.crypto == "aes"):
        args.message : str | None = input()
        if (args.message == None):
            raise ValueError("no message input")
        aes = Aes(args)
        if (args.mode == "cipher"):
            aes.cipher()
            return 0
        if (args.mode == "decipher"):
            aes.decipher()
            return 0
        raise ValueError("Invalid mode")

    raise ValueError("Invalid crypto mode")