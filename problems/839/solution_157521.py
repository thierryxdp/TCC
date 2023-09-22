import math
def carros(passageiros,capacidade=5):
    '''
    Retorna o número (inteiro) de veículos de certa capacidade (default=5) necessários
    para transportar um número de passageiros.
    '''
    return math.ceil(passageiros/capacidade)