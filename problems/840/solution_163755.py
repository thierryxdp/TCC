from math import *

def trigo(a):
    """calcula quantos bolos podem ser feitos com a quantidade de xícaras de trigo a; in, int -> int"""
    return floor(a/2)

def ovo(b):
    """calcula quantos bolos podem ser feitos com a quantidade de ovox b; int, int-> int"""
    return floor(b/3)

def leite(c):
    """calcula quantos bolos podem ser feitos com a quantidade de colheres de sopa de leite c; int, int -> int"""
    return floor(c/5)

def bolos(a,b,c):
    """calcula quantos bolos podem ser feitos, no máximo, com as quantidades fornecidas de trigo, ovo e leite (a, b e c respectivamente); int, int -> int"""
    return min(trigo(a),ovo(b),leite(c))