from math import *
def carros(n,c=5):
    if n<=c and n!=0:
        return 1
    elif n>c:
        return ceil(n/c)
    else:
        return 0