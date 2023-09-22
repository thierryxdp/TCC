from math import *
def primo(m):
    l=ceil(m/2)
    for i in range(1,l+2):
        if m%i==0:
            return False
        else:
            return True