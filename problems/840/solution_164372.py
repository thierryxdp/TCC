import math

def bolos(a,b,c):
    """Calcula e retorna a quantidade de bolos que podem ser obtidos 
	através dos ingredientes: A xícaras, B ovos, C colheres;"""
    return math.floor(min(a/2,b/3,c/5))