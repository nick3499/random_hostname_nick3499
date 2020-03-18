#! /bin/python3
'''`random_hostname` module contains the `rand_hostname()` method \
which generates a pseudo-random hostname.'''
from random import randrange
from subprocess import run

def rand_az():
    '''Return random character: a...z'''
    return chr(randrange(97, 123, 1))

def rand_AZ():
    '''Return random character: A...Z'''
    return chr(randrange(65, 91, 1))

def rand_09():
    '''Return random character: 0...9'''
    return chr(randrange(48, 58, 1))

def rand_hostname():
    '''Set psuedo-random system hostname.'''
    rand_host = f'{rand_az()}{rand_AZ()}{rand_09()}{rand_az()}{rand_AZ()}{rand_09()}'
    run(['sudo', 'hostnamectl', 'set-hostname', rand_host], check=True)

if __name__ == '__main__':
    rand_hostname()
