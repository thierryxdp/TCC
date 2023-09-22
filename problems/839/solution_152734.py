def carros (pessoas,capacidade=5):
    """calcular e retornar o número exato de carros necessários para a viagem, dados o número de pessoas e a capacidade do carro"""
    """int,int->int"""
    return max (pessoas/capacidade)