import math
def bolos (a,b,c):
    '''Dado o número de xícaras de farinha de trigo a, o de ovos b e o de colheres de sopa de leite c, calcule quantos bolos podem ser feitos; int,int,int -> int'''
    A=math.floor(a/2)
    B=math.floor(b/3)
    C=math.floor(c/5)
    return min(A,B,C)