from math import floor
def bolos(A,B,C):
    '''Recebe a quantidade de xícaras de farinha, ovos e colheres de sopa de leite disponíveis e retorna a quantidade de bolos que podem ser feitos; int, int, int -> int''' 
    return min(floor(A/2), floor(B/3), floor(C/5))