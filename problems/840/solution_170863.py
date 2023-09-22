import math
def bolos(A,B,C):
    '''Calcula a quantidade maxima de ingredientes dados ingredientes minimos
entrada: int, int, int, 
saida: int'''
    a = A // 2 
    b = B // 3
    c = C // 5
	if a <= b and a <= c:
        return a
    if b <= a and b <= c:
        return b
    if c <= a and c <= b:
        return c