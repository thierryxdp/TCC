import math
def num_bombons(D,P):
'''Função que retorna o máximo de números bombons que é possível comprar
dado o dinheiro disponível e o preço de cada bombom; 
float,float->int'''
    return math.ceil(D//P)