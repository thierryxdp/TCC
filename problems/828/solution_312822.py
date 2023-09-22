from math import *
def primo(n):
    
    if n<= 1:
        return False
    elif n>=2:
        return True
    for p in range(2,n):
        if (n%p)=0:
            return False