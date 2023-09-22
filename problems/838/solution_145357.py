import math
def num_bombons(dinheiro,custo_bombom):
    'Função que dados o dinheiro total e o custo de um bombom, quantos bombons uma pessoa consegue comprar.'
    return math.floor(dinheiro/custo_bombom)