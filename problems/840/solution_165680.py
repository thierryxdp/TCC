import math
def bolos (A: int, B: int, C: int)-> int:
    """retorna a quantidade máxima de bolos que João consegue fazer, dado o 
    número de xícaras de farinha A, de ovos B e de colheres de sopa de 
    leite C disponíveis"""
    return min(math.floor(A/2), math.floor(B/3), math.floor(C/5))