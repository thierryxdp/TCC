import math
def bolos(A,B,C):
    ''' calcula a quantidade máxima de bolos que ele consegue fazer, dado uma quantidade de ingredientes '''
    return min(A//2,B//3,C//5)