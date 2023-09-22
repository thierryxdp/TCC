import math

def farinha(a):
    ''' Calcula e arredonda para baixo o numero necessario de farinha para a produção do bolo '''
    return math.floor(a/2)

def ovos(b):
    ''' Calcula e arredonda para baixo o numero necessario de ovos para a produção do bolo '''
    return math.floor(b/3)

def leite(c):
    ''' Calcula e arredonda para baixo o numero necessario de leite para a produção do bolo '''
    return math.floor(c/5)

def bolos(a,b,c):
    ''' retorna a quantidade de bolos possiveis para fazer com a quantidade de ingredientes disponiveis '''
    ''' float, float, float ---> int '''
    return min(farinha(a),ovos(b),leite(c))