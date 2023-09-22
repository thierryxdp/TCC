import math
def bolos (a,b,c):
    """Calcula quantas vezes a mais João possui certo ingrediente em relação à receita e seleciona aquele que daria para fazer menos receitas""" 
    return min(a//2,b//3,c//5)