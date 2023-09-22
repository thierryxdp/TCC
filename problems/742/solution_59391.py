import math
from math import *
def substitui(s,x,i):
    if (len(x)!=1):
        return False
    if (i <0 or i> len(s)-1):
        return 'O numero inteiro deve estar entre 0 e o comprimento da string'
    return s[:i-1]+x+s[i:]