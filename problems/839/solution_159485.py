def carros(p,c=5):
    '''dada a quantidade de pessoas a funcao calcula
    quantos carros serao necessarios para essa viagem,
    sendo que cada carro transpora ate 5 passageiros,
    caso contrario sera informado tambem a capacidade
    dos carros, considerando que todos os veiculos
    suportam a mesma quantidade de pessoas'''
    import math
    return math.ceil(p/c)