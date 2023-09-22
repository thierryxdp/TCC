import math
def carros(num_pessoas,car=5):
    '''
    dados o numero de pessoas e a quantidade 
    que o carro suporta das mesmas, quando for diferente
    de 5, a função calcula e retorna a quantidade 
    de carros que será preciso. 
    int --> int 
    '''
    x = num_pessoas/car
    return math.ceil(x)