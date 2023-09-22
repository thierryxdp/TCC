from math import *
def primo(n):
    for i in range(2,round(sqrt(n)+1)):
        if n%i == 0:
            return False
    return True