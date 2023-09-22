import math
def num_bombons(dinheiro, valor_bombom):
    '''Função que calcula e retorna a maior quantidade de bombons que é possivel comprar com uma determinada quantia. int, float -> float'''
    return math.floor(dinheiro/valor_bombom)