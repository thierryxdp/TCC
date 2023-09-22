def carros(p,c=5):
    '''dada a quantidade de pessoas a funcao calcula
    quantos carros serao necessarios para essa viagem,
    sendo que cada carro transpora ate 5 passageiros'''
    import math
    return mth.ceil(p/c)