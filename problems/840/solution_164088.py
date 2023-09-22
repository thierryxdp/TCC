from math import floor
def bolos(A,B,C):
    """
    Função que determina qual a quantidade máxima de bolos que se consegue fazer seguindo a receita:
    2x ingrediente A (xícara de farinha de trigo)
    3x ingrediente B (ovo)
    5x ingrediente C (colhere de sopa de leite)
    """
    return min(floor(A/2), floor(B/3), floor(C/5))