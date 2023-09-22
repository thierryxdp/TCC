def carros(pessoas, capacidade=5):
    """calcula o numero de carros necessarios para transportar um certo numero de pessoas dado esse numero e a capacidade do carro"""
    import math
    return math.ceil(pessoas/capacidade)