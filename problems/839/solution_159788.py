def carros(amigos):
    '''funcao que calcula a quantidade de carros 
    necessarios para uma viagem entre amigos, sabendo
    que a capacidade convencional de pessoas num carro
    é 5. obs: os carros são todos iguais.'''
    c = amigos/5
    carros = round(c)
    return carros