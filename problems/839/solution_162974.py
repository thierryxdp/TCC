import math
def carros(passageiros):
    """Calcula o numero de carros necessarios para uma viagem, baseado na lei estadual de apensa 5 pessoas por carro"""
    n_p_c=passageiros/5
    n_p_c=math.ceil(n_p_c)
    return n_p_c