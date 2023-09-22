import math
def bolos (A,B,C):
    "Calcula o numero maximo de bolos possiveis seguindo a receita"
    bolos=2A+3B+5C
    return math.floor(min(A/2,B/3,C/5))