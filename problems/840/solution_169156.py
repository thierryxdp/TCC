import math
min
def bolos(farinha,ovos,leite):
    '''Esta funçao calcula o numero maximo de bolos que 
    pode se fazer com os ingredientes disponíveis, dado a 
    quantidade de farinha, ovos e leite disponíveis'''
    qtd farinha = farinha//2
    qtd ovos = ovos//2
    qtd leite = leite //5
    return min (farinha,ovos,leite)