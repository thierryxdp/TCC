import math

def carros(pessoas,capacidade=5):
    """retorna o numero exato de carros necessarios dados o numeros de pessoas e a capacidade do veiculo
       int, int -> int"""
    return math.ceil(pessoas/capacidade)