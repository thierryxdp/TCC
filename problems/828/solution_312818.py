from math import *
def primo(n):
    divisoresN = divisores(n)
    if divisoresN <= 1:
        return False
    elif divisoresN>=2:
        return True
    for p in range(2,n):
        if (n%p)==0:
            return False