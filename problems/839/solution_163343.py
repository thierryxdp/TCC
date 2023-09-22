import math
def carros(nPessoas,capacidade=5):
    '''Recebe o numero de pessoas e retorna o numero de carros neces-
    sario para realizar a viagem; int->int'''
    
    qtd=math.ceil(nPessoas/capacidade)
    
    return qtd