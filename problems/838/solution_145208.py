#Bombons
import math
def num_bombons (dinheiro, preco):
    '''Função que calcula e retorna o maior número de bombons possível
    ao dvidir o valor do dineiro que Pedrinho possui pelo preço do bombom
    float, float=>int'''
    return math.ceil(dinheiro//preco)