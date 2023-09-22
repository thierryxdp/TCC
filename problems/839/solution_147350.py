import math
def carros(pessoas,vagas=5):
    '''essa função calcula o número de carros necessários para fazer uma viagem dados:pessoas e vagas(padrão 5)'''
    return math.ceil(pessoas/vagas)