import math
def carros(pessoas,capacidade=5):
    """Esta função calcula e retorna o número exato de carros necessários para fazer uma viagem.
       Caso a capacidade não seja dada a capacidade do carro será igual a 5"""	
    return math.ceil(pessoas/capacidade)