import math
def carros(nPessoas, capCarro=5):
    '''calcular e retornar o numero exato
de carros necessarios para a viagem, dado o quantitativa de pessoas'''
    return math.ceil((nPessoas/capCarro))