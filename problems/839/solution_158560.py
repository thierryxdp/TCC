from math import *
def carros(p,c=5):
    '''função q calcula o numero de carros necessários para 
    comportar um dado numero de pessoas p, caso o numero da 
    capacidade dos carros c nao seja informado será assumido
    como a capacidade de um veiculo normal c=5 '''
    return ceil(p,c)