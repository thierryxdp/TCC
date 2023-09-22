import math
def bolos(A,B,C):
    '''calcula e retorna a quantidade de bolos que podem ser feitos'''
    return min(math.round(A/2),math.round(B/3),math.round(C/5))