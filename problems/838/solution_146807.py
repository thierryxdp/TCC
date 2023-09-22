import math
def num_bombons(dinheiro,preço):
    """Função que dados o dinheiro e o preço do bombom como
    entradas, calcula o maior número de compra de bombons possíveis
    float, float  -> int"""
    
    return math.floor(dinheiro/preço)