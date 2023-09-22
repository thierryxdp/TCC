import math
def bolos(a,b,c):
    """Retorna a quantidade maxima de bolos inteiros que pode ser feita 
    com os materias fornecidos xicaras de farinha, ovos e colheres leite
    respectivamente."""
    return math.floor(min(a//2,b//3,c//5))