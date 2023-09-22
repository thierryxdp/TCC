import math
def num_bombons (dinheiro, preçoBombons):
    'Função que calcula o numero de bombons possiveis de comprar dado seu preço e o dinheiro'
    return math.round (dinheiro // preçoBombons)