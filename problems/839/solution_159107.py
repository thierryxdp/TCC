from math import ceil
def carros(pessoas,capacidade=5):
    '''Calcula e retorna a quantidade de carros necessários para uma viagem
    	int,int -> int'''
    
    return ceil(pessoas/capacidade)