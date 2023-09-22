import math
def bolos(a,b,c):
    '''funçao que diz qual a quantidade máxima de bolos que
    João consegue fazer;int,int,int->int'''
    return min(a//2,b//3,c//5)