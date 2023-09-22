#recebe o total de passageiros e retorna quantos veículos seriam necesários para transporta-los
import math

def carros(pessoas=22, capacidade=5):
    '''(int,int=>int)'''
    automoveis = math.ceil(pessoas/capacidade)
    return automoveis