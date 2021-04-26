#!/usr/bin/env python
# -*- coding: utf8 -*-
import string
import itertools
"""
Helpers for en- and decrypting using the Vigenère or Caesar ciphers.
(The Caesar cipher is a special case of Vigenère with a key length of one.)
"""

CHARS = string.ascii_letters

def envig(text, key):
    return ''.join(vig_(text, key, +1))

def devig(text, key):
    return ''.join(vig_(text, key, -1))

def usekey(key, op):
    for c in itertools.cycle(key.upper()):
        if c not in string.ascii_uppercase:
            raise ValueError('Key must only contain letters from A-Z')
        yield op * (ord(c) - ord('A'))

def offset(c, num):
    if c in string.ascii_lowercase:
        alph = string.ascii_lowercase
    elif c in string.ascii_uppercase:
        alph = string.ascii_uppercase
    else:
        return c

    return alph[(ord(c)-ord(alph[0]) + num) % 26]

def vig_(text, key, op):
    # op is +1 for encryption, -1 for decryption
    keychars = usekey(key, op)
    for c in text:
        if c in CHARS:
            yield offset(c, next(keychars))
        else:
            yield c

def ungerman(text):
    repl = {
        'Ä':'AE',
        'Ö':'OE',
        'Ü':'UE',
        'ä':'ae',
        'ö':'oe',
        'ü':'ue',
        'ß':'ss',
    }
    for fr, to in repl.items():
        text = text.replace(fr, to)
    return text
