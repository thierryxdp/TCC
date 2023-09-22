def carros(pessoas, capacidade=5):
    '''função que recebe o numero de pessoas e a
    capacidade e retorna a quantidade de carros necessária)'''
    return math.ceil(pessoas/capacidade)