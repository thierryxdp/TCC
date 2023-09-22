import math
def carros(pessoas,capacidade=5):
    '''Função que calcula quantos carros são necessários
    para transportar um dado número de pessoas. Se a capacidade
    do carro não for informada, o valor estimado será 5'''
    return math.ceil(pessoas/capacidade)