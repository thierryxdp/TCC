import math
def bolos(A,B,C):
    "retorna a quantidade máxima de bolos que podem ser feitos"
    return min(math.fabs(A/2, B/3, C/5))