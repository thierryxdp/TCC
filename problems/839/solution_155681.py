def carros(pessoas, capacid=5):
    import math
    '''
Funcao que calcula e retorna o numero exato de carros necessarios
para esta viagem, considerando que seja dado como entrada o numero de pessoas.
int, int=>int
    '''
    automoveis=math.ceil(pessoas / capacid)
    return automoveis