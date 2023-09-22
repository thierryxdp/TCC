import math
def carros(pessoas,vagas_no_veiculo=5):
    '''função calcula x carros necessarios p viagem'''
    return math.ceil(pessoas/vagas_no_veiculo)