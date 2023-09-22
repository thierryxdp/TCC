import math
def bolos(A,B,C):
    '''Calcula a quantidade maxima de ingredientes dados ingredientes minimos
entrada: int, int, int, 
saida: int'''
	a = A // 2 
    b = B // 3
    c = C // 5
    return min([a,b,c])