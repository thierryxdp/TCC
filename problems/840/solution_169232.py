import math
def bolos(farinha,ovos,leite):
    ''' Calcula o número máximo de bolos que podem ser feitos com os ingredientes dispomiveis,
    dado a quantidade de farinha =a, ovos = b e leite =c disponíveis. '''
    qtd_farinha = farinha//2
    qtd_ovos = ovos//3
    qtd_leite = leite//5
    return min(qts_farinha, qtd_ovos,qtd_leite)