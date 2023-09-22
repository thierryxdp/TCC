from math import floor

def num_bombons(dinheiro,preco_unid):
    '''função que retorna a maior quantidade de bombons que podem ser comprados
dado o dineiro e o preço do bombom'''
    return floor(dinheiro/preco_unid)