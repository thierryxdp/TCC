import math
def carros (num_pessoas, capac_carro = 5):
    '''Retorna a quantidade de carros necessaria para fazer uma viagem em base da quantidade de passageiros e da capacidade do modelo do carro a ser utilizado;
    int, int -> int'''
    return math.ceil(num_pessoas//capac_carro)