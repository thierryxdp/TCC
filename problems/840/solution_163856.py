import math
def bolos (A,B,C):
    "retorna a quantidade de bolos que podem ser feitos diante da quantidade de ingredientes A farinha de trigo, B ovos e C leite"
    return min(A//2, B//3, C//5)