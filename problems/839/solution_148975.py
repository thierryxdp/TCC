import math as m

def carros(p,c=5):
    '''Entre com o numero de pessos(p), caso queira, entre com o valor da
    capacidade do automovel, padrão = 5'''
    return m.ceil(p/c)