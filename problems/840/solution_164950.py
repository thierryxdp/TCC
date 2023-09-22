from builtins import *

def bolos(A,B,C):
    ''' Calcula a quantidade máxima de bolos que podem ser feitos dados
    as quantidade de xícaras de farinha (A), ovos (B) e colheres de sopa
    de leite (C)
    int, int, int -> int '''
    
    return min(A//2,B//3,C//5)