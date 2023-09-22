def carros(pessoas,carro=5):
    '''funcao que calcula a quantidade de carros, nao convencionais, dada a quantidade de pessoas'''
    if pessoas/carro==int(pessoas/carro):
        return pessoas//carro
    else:
        return pessoas//carro+1