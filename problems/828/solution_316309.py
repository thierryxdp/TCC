from math import *
def primo(m):
    l=ceil(m/2)
    for i in range(2,l+1):
        if m%i==0:
            return False
    return True