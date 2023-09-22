def carros(num_passageiros, capacidade=5):
    """Função que calcula a quantidade de carros que são necessárias para realizar uma viangem dado um numero x de passageiros
    INT, INT -> INT"""
    import math
    veiculos = math.ceil(num_passageiros/capacidade)
    return veiculos