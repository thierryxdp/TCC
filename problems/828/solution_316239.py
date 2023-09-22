from math import *
def primo(num):
    ''' determina se um número é primo ou não;
    int->bool'''
    for n in range(2,ceil(num/2)):
        if num%n==0:
            return False
    return True