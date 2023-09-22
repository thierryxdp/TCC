def carros(pessoas,capacidade = 5):
    '''A funcao deve dividir o numero de pesssoas pela 
    capacidade e ter como resultado o numero de carros;
    int, int, -> int'''
    carros= math.ceil(pessoas/capacidade)
    return carros