from math import floor
def num_bombons(dinheiro, preco_bombom):
    '''Função que calcula o número de bombons que
    Pedrinho pode comprar, dado o quanto de dinheiro
    ele tem e o valor do bombom
    float, float -> int'''
    return floor(dinheiro/preco_bombom)