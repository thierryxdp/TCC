import math

def carros(numPessoas,vagas=5):
    ''' Calcula o nume de carros necessarios para carregar uma guantidade x de
    pessoas
    '''
    return math.ceil numPessoas/vagas