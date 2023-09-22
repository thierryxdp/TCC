import math
def carros (pessoas, capacidade=5):
    """Calcula o número de carros necessários para fazer uma viagem,
    dados o número de pessoas e a capacidade do carro utilizado. Caso a 
    capacidade não seja infromada, será considerado o valor 5."""
    return math.ceil(pessoas/capacidade)