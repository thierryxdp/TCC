from math import*
def carros(pessoas,carros=5):
    """calcula o numero de carros necessarios para transportar certo numero de pessoas. Caso nao seja dado um valor na capacidade do carro, sera considerado uum carro de 5 lugares"""
    return round(pessoas//carros)