from math import *

def trigo(a):
    return floor(a/2)

def ovo(b):
    return floor(b/3)

def leite(c):
    return floor(c/5)

def bolos(a,b,c):
    return min(trigo(a),ovo(b),leite(c))