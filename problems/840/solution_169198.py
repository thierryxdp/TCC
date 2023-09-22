import math
def bolos(farinha,ovos,leite):
    '''Esta funçao calcula o numero maximo de bolos que 
    pode se fazer com os ingredientes disponíveis, dado a 
    quantidade de farinha, ovos e leite disponíveis'''
    qtd_farinha = farinha//2
    qtd_ovos = ovos//2
    qtd_leite = leite //5
    return min(qtd_farinha, qtd_ovos, qtd_leite)