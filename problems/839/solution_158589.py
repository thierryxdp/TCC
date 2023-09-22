def carros(pessoas,capacidade=5):
    '''Esta função calcula e retorna o número exato de carros 
    com capacidade para 5 pessoas necessários para uma viagem'''
    return math.ceil(pessoas/capacidade)