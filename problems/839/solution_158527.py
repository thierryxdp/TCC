import math

def carros(capacidade=5):
    '''
    	Função que retorna o numero de carros necessários
        para levar uma certa quantidade de pessoas.
    '''
    
    carro = math.ceil(numPessoas/capacidade)
    
    return carro