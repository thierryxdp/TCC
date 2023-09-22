import math
def carros(pessoas,capacidade=5):
    """Função que calcula o número de carros exatos necessários uma viagem dadas a quantidade de pessoas e a capacidade padrão dos veiculos"""
    """(int, int->int)"""

   automoveis = math.ceil(pessoas / capacidade)

   return automoveis