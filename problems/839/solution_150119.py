import math
def carros(x,c=5):
    '''função que calcula o numero de carros necessarios numa viagem, dados o número de pessoas e a capacidade do carro(somente necessário caso seja diferente de 5);int,int-->int'''
    return math.ceil(x/c)