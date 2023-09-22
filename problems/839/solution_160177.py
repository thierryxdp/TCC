from math import*
def carros(pessoas,capacidade=5):
    '''funcao que calcula a quantidade exata de carros 
necessarios para fazer uma viagem considerando a capacidade 
do carro e a quantidade de pessoas; int,int-->int'''
    return ceil(pessoas/capacidade)