import math
def bolos(a,b,c):
    '''funcao que calcula a quantidade de bolos
    que podem ser feitos a partir de uma receita e
    uma dada quantidade de ingredientes'''
    return math.floor(min(a/2,b/3,c/5))