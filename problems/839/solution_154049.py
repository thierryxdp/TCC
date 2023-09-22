from math import ceil
def carros(p, c=5):
    '''funcao que retorna o numero de carros necessarios para a viagem dadas a quantidade
    de pessoas p que irao viajar e a capacidade c dos veiculos; int, int -> int'''
    return ceil(p/c)