#! /bin/python3
'''`random_hostname` module contains the `rand_hostname()` method \
which generates a pseudo-random hostname.'''
from random import randrange
from subprocess import run


def rand_hostname():
    '''`rand_hostname()` method generates a 6-char pseudo-random hostname.'''
    rand_chars = []
    # append random chars
    for _ in range(2):
        rand_chars.append(chr(randrange(97, 123))) # append char (a to z)
        rand_chars.append(chr(randrange(65, 92)))  # append char (A to Z)
        rand_chars.append(chr(randrange(48, 58)))  # append char (0 to 9)
    # set random hostname
    run(['sudo', 'hostnamectl', 'set-hostname', ''.join(rand_chars)], check=True)


if __name__ == '__main__':
    rand_hostname()
