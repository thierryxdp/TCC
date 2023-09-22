import math
def carros(pessoas,lugares=5):
    '''
    função vai dividir o valor de pessoas por 5 lugares no carro,
    e utilizando o math.ceil, ira retonar para o numero int.
    '''
    return math.ceil(pessoas/lugares)