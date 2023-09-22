import math
def num_bombons(d,p):
 """Retorna o maior número de bombons possiveis para comprar com o dinheiro disponivel, dado o dinheiro e o preço do bombom 
    float, float => int """
 return math.floor(d/p)