import math
def carros(p,c=5):
    '''função que calcula o numero de carros necessários para 
    comportar um dado numero de pessoas p, caso o numero da 
    capacidade dos carros c não seja informado sera assumido 
    como a capacidade de um veículo normal'''
    return math.ceil(p/c)