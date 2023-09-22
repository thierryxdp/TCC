import math
def bolos (A,B,C):
    "Calcula o numero maximo de bolos possiveis seguindo a receita"
    return math.floor(min(A/2,B/3,C/5))