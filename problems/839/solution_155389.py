from math import *
def carros(n,c=5):
    if n<=c:
        return 1
    elif n>c:
        return ceil(n/c)
    elif n==0:
        return 0