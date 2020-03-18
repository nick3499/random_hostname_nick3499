#! /bin/python3
'''`random_hostname` module contains the `rand_hostname()` method \
which generates a pseudo-random hostname.'''
from random import randrange
from subprocess import run


def rand_hostname():
    '''`rand_hostname()` method generates a pseudo-random hostname.'''
    # alphanumeric collection
    _alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    _num = '0123456789'
    rand_letters = []
    rand_numbers = []
    # append random letters to list
    for _ in range(4):
        rand_int = randrange(0, 52)  # rand int
        rand_letters.append(_alph[rand_int])  # append 4 rand indexed letters
    # append random numbers to list
    for _ in range(2):
        rand_num = randrange(0, 10)  # rand int
        rand_numbers.append(_num[rand_num])  # append 2 rand indexed numbers
    # set random hostname
    rand_host = ''.join(rand_letters) + ''.join(rand_numbers)
    run(['sudo', 'hostnamectl', 'set-hostname', rand_host], check=True)


if __name__ == '__main__':
    rand_hostname()
