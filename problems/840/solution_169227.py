import math
def bolos(a,b,c):
    ''' Calcula o número máximo de bolos que podem ser feitos com os ingredientes dispomiveis,
    dado a quantidade de farinha =a, ovos = b e leite =c disponíveis. '''
    qtd_farinha = a//2
    qtd_ovos = b//3
    qtd_leite = c//5
    return min(qts_farinha, qtd_ovos,qtd_leite)