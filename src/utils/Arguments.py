##
## EPITECH PROJECT, 2023
## crypto
## File description:
## Arguments
##

from argparse import SUPPRESS, ArgumentError, ArgumentParser, BooleanOptionalAction

class IArgs():
    crypto: str | None
    mode: str | None
    block: bool
    key: str | None
    public_key: str | None
    private_key: str | None
    message: str

class Flag():
    xor: bool
    aes: bool
    rsa: bool
    c: bool
    d: bool
    g: list
    b: bool
    key: str | None

class Argument():
    def __init__(self: IArgs) -> None:
        self.crypto: str | None = None
        self.mode: str | None = None
        self.block: bool = False
        self.key: str | None = None
        self.public_key: str | None = None
        self.private_key: str | None = None
        self.message: str = ""

    def set_args(self: IArgs, args: Flag) -> None:
        if hasattr(args, "xor") and args.xor:
            self.crypto = "xor"
        elif hasattr(args, "aes") and args.aes:
            self.crypto = "aes"
        elif hasattr(args, "rsa") and args.rsa:
            self.crypto = "rsa"
        if hasattr(args, "c") and args.c:
            self.mode = "cipher"
        elif hasattr(args, "d") and args.d:
            self.mode = "decipher"
        elif hasattr(args, "g") and args.g:
            self.mode = "generate"
            self.public_key = args.g[0]
            self.private_key = args.g[1]
        if hasattr(args, "b") and args.b:
            self.block = True
        if hasattr(args, "key") and args.key:
            self.key = args.key


    def check_args(self: IArgs) -> bool:
        if self.crypto is None or self.mode is None:
            return False
        if self.mode == "generate":
            if self.crypto != "rsa" or self.block or self.private_key is None or self.public_key is None:
                print(self.private_key, self.public_key)
                return False
            return True
        if self.block and self.crypto == "rsa":
            return False
        if self.key is None:
            return False
        return True

def parse_args() -> IArgs | None:
    parser = ArgumentParser(exit_on_error=False, add_help=False)
    group_mode = parser.add_mutually_exclusive_group(required=False)
    group_cipher = parser.add_mutually_exclusive_group(required=False)

    parser.add_argument("-h", action="help", help="Show this help message and exit", default=SUPPRESS)
    parser.add_argument("-g", metavar=('P', 'Q'), nargs=2,
                        help="for RSA only: generate a public and private key pair from the prime number P and Q")
    group_mode.add_argument("-xor", help="computation using XOR cryptorithm", default=SUPPRESS,
                            action=BooleanOptionalAction)
    group_mode.add_argument("-aes", help="computation using AES cryptorithm", default=SUPPRESS,
                            action=BooleanOptionalAction)
    group_mode.add_argument("-rsa", help="computation using RSA cryptorithm", default=SUPPRESS,
                            action=BooleanOptionalAction)
    group_cipher.add_argument("-c", help="MESSAGE is clear and we want to cipher it", default=SUPPRESS,
                              action=BooleanOptionalAction)
    group_cipher.add_argument("-d", help="MESSAGE is cipher and we want to decipher it", default=SUPPRESS,
                              action=BooleanOptionalAction)
    parser.add_argument("-b",
                        help="block mode: for xor and aes, only works on one block MESSAGE and KEY must be of the "
                             "same size",
                        default=SUPPRESS, action=BooleanOptionalAction)
    parser.add_argument("key", type=str, nargs="?")
    try:
        argument: IArgs = Argument()
        args: Flag = parser.parse_args()
        argument.set_args(args)
        if argument.check_args():
            return argument
        else:
            return None
    except ArgumentError as error:
        print(error)
        return None
