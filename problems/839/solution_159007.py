import math 
def carros(pessoas, n_carros=5):
    '''Retorna a quantidade de carros necessários 
    para a viagem dado o numero de amigos, caso o
    número de carros não sejam de capacidades
    convencionais, também será dado como entrada a
    capacidade dos veículos'''
    return math.ceil(pessoas/n_carros)