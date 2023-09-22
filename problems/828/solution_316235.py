from math import *
def primo(num):
    ''' determina se um número é primo ou não;
    int->bool'''
    for n in range(2,num):
        if num%n==0:
            return False
    return True