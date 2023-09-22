from math import *
def primo(m):
    l=ceil(m/2)
    for i in range(2,m):
        if m%i==0:
            return False
        else:
            return True