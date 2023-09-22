import math
def bolos(A,B,C):
    '''calcula e retorna a quantidade de bolos mínima que Joao pode fazer com A, B e C ingredientes'''
    return min(math.floor(A/2), math.floor(B/3), math.floor(C/5))