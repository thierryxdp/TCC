import math
def bolos(A,B,C):
    "retorna a quantidade máxima de bolos que podem ser feitos"
    return math.ceil(min(A/2, B/3, C/5))