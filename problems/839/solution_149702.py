>>> import math
>>> def carros(p,c=5):
    '''Função que calcula número de carro(s) necessário(s) com capacidade (c) para um dado número de pessoas(p)'''
    return math.ceil(p/c)