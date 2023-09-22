from import math.ceil 
def carros(p,c=5):
    '''Essa funcao retorna, dados p= quantidade de pessoas e c=capacidade 
    do carro, a quantidade exata de carros necessarios para uma viagem'''
    return math.ceil(p/c)