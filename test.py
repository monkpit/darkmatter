#! /usr/bin/env python

from argparse import ArgumentParser
argparser = ArgumentParser(description=("Tests for DarkStar FFXI"
                                        "Server Emulator."))


class args(object):
    def __init__(self, name, helptext=None, action='store'):
        argparser.add_argument(name, help=helptext, action=action)

    def __call__(self, f):
        return f


@args('--login', action='store_true')
def test_dsconnect_server(ip, port):
    pass


def run(args):
    if args.login:
        from FFXI.character import authenticate_character
        result = authenticate_character(char_name="higeki", password="9908653782")
        print(result)
    return 0

if __name__ == "__main__":
    import sys
    sys.path.append('src')
    args = argparser.parse_args()
    sys.exit(run(args))
