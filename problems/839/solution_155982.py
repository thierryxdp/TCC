def carros (p):
    '''calcular a quantidade de veículos necessários para transportar um grupo de amigos, levando em consideração o limite de 5 passageiros
por carro, sendo p o número de amigos.'''
    return math.ceil (p/5)