import math
def hashtag(x):
    'adiciona # no inicio, meio e final de uma string'
    'entrada: string'
    'saida: string'
    a=math.floor(len(x)/2)
    dividir1=x[:a]
    dividir2=x[a:]
    soma= '#'+dividir1+'#'+dividir2+'#'
    return soma