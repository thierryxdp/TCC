import math
def bolos(A,B,C):
    '''determina qual a quantidade máxima de bolos que ele consegue fazer;
    int,int,int -> int'''
    return min(A//2,B//3,C//5)