import math

def carros(pessoas, capacidade=5):
     '''recebe a quantidade de pessoas e a capacidade do carro e 
    retorna a quantidade de carros necessária. int, int=int'''
    x=pessoas/capacidade
    return math.ceil(x)