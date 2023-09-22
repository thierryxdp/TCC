#Quantos carros
import math
def carros (pessoas, capacidade=5):
    '''Função que calcula e retorna a divisão do números de 
    pessoas pela capacidade que cada carro suporta ter
    int, int=>int'''
    return math.ceil(pessoas//capacidade)