import math
def bolos(a,b,c):
    '''funçao para calcular a quantidade maxima de bolos dados a,b,c; int,int,int->int'''
    return min(a//2,b//3,c//5)