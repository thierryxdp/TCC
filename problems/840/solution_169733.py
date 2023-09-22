import math
def bolos(A,B,C):
    '''calcula e retorna a quantidade de bolos mínima que Joao pode fazer com A, B e C ingredientes'''
    return math.floor((A/2+B/3+C/5)/3)