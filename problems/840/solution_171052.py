import math
def bolos (a,b,c):
    '''funçao para calcular o numero minimo de bolos que podem ser feitos dados a,b,c;int,int,int->int'''
    return min (a//2,b//3,c//5)