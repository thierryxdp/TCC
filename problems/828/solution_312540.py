from math import *
def primo(n):
    divisoresN = divisores2(n)
    if divisoresN > 2:
        return False
    else:
        return True