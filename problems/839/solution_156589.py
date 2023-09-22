import math

def carros(numPessoas, capacidade=5):
    '''
    	Função que retorna o numero de carros necessários
        para levar uma certa quantidade de pessoas.
    '''
    
    carro = math.ceil(pessoas/capacidade)
    
    return carro