from math import *
ef primo(n):
    divisoresN = divisores(n)
    if divisoresN > 2:
        return False
    else:
        return True