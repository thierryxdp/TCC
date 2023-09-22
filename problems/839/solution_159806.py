import math
def carros(amigos,veiculos=5):
    '''funcao que calcula a quantidade de carros 
    necessarios numa viagem entre amigos, sendo considerado
    5 a capacidade convencional de pessoas em um unico carro.'''
    carros = math.ceil(amigos / 5) 
    c = round(carros + 0.5)
    return c