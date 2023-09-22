import math
def carros(pessoas,veiculo=5):
    '''calcula o numero de veiculos necessarios para 
    transportar certo numero de pessoas'''
    return math.ceil(pessoas/veiculo)