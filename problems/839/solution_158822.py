import math
def carros(pessoas,espaco=5):
    """calcula quantos carros serão usados na viagem, dado o numero de pessoas e o espaço no carro. Se nao dado o espaço no carro sera usado 5"""
    return math.ceil(pessoas/espaco)