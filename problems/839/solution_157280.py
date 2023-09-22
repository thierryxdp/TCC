from math import ceil
def carros(n,c=5):
    '''
    	A função irá definir quantos carros
        serão necessários para transportar
        um número n de passageiros, com a capacidade
        c de cada carro sendo 5 quando não especificada
    
    '''
    return ceil(n/c)