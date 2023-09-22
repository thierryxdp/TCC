from math import floor

def bolos(A=2,B=3,C=5):
    """Calcula e retorna a quantidade de bolos que joão consegue fazer, dados as quantidades de ingredientes """
    return floor((A+B+C)/10)