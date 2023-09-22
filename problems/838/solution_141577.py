import math
def num_bombons(dinheiro, preco_bombom):
    '''Função que retorna o maior número de bombons possíveis de comprar
    dado o dinheiro disponível e o preço do bombom'''
    return math.ceil(dinheiro/preco_bombom)