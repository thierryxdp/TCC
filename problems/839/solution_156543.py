import math
def carros (pessoas,capacidade=5):
    carro=math.ceil(pessoas/capacidade) 
    ''' Essa função retorna a quantidade de carros 
para carregar um certo numero de pessoas;
int,int->int '''
    
    return carro