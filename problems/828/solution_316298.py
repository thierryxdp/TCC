def primo(m):
    from math import *
    l=ceil(m/2)
    for i in range(2,l):
        if m%i==0:
            return False
        else:
            return True