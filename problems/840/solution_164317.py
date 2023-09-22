def bolos(A,B,C):
    "retorna a quantidade máxima de bolos que podem ser feitos"
    return math.floor(min(A/2, B/3, C/5))