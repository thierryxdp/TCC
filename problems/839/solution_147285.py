def carros(npessoas,ncarros=5):
    '''Quando inseridos o número de pessoas(n pessoas), e o número de assentos no carro, se ncarros é diferente de 5, retorna o número exatos de carro necessários'''
    return math.ceil(npessoas/ncarros)