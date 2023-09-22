import math

def bolos(A=2,B=3,C=5):
    """Calcula e retorna a quantidade de bolos que joão consegue fazer, dados as quantidades de ingredientes """ 
    lista=(A/2,B/3,C/5)
    return math.floor(min(lista))