from math import *
def primo(n):
    divisoresN = divisores(n)
    if divisores(n) > 2:
        return False
    else:
        return True