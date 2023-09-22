from math import ceil 
def carros(pessoas,veiculos=5):
    '''funcao que calcula o numero de carros necessarios para a viagem'''
    return ceil (pessoas/veiculos)