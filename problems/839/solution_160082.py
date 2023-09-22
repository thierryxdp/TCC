def carros(passageiros,capacidade_carro=5):
    """Calcula o numero de carros necessarios para uma viagem, baseado na lei estadual
    de apensa 5 pessoas por carro"""
    n_p_c=passageiros/capacidade_carro
    n_p_c=math.ceil(n_p_c)
    return n_p_c