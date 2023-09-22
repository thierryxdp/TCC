def carros(pessoas,capacidade=5):
    '''
    funcao que divide a quantidade de pessoas pela capacidade de carros
    e retorna o valor necessário de automoveis, alem de passar para o 
    maior inteiro caso a divisao resulte num float
    int,int---->int
    '''
    import math
 
    carros=math.ceil(pessoas/capacidade)
    
    return carros