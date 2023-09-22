import math
def arredondamento(x):
    '''funçao que arrendoda um valor decimal x para cima'''
    return round(x-0.5)

def compraBombom(dinheiro,preço):
    """Função que dados o dinheiro e o preço do bombom como
    entradas, calcula o maior número de compra de bombons possíveis
    float, float  -> int"""
    return round(dinheiro/preço)