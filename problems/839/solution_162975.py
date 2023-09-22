import math
def carros(passageiros, capacidade = 5):
    """Calcula o numero de carros necessarios para uma viagem, baseado na lei estadual de apensa 5 pessoas por carro"""
    n_p_c=passageiros/capacidade
    n_p_c=math.ceil(n_p_c)
    return n_p_c