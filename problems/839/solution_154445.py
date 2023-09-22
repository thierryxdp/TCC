import math
def carros(x,y=5):
    '''Função que calcula a quantidade de carros necessários para uma de viagem de uma grupo de amigos 
    sendo x a quantidade de pessoas que vai na viagem e Y a quantidade de pessoas que cabem no carro, podendo alterar esse valor'''
    return math.ceil(x/y)