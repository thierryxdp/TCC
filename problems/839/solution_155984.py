import math
def carros(pessoas, capacidade):
    """Função que calcula o número de carros exatos necessários uma viagem dadas a quantidade de pessoas e a capacidade padrão dos veiculos"""
    car = pessoas/capacidade
    return math.ceil(car)