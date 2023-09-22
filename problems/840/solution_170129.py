from math import floor
def bolos(farinha,ovo,leite):
    '''Função que calcula e retorna a quantidades de bolos, dividindo o números de ingredientes necessários com a quantidade existente, arredondando para baixo e pegamos o menor valor de entrada
        int, int→int'''
    a = floor(farinha / 2) 
    b = floor(ovo / 3) 
    c = floor(leite / 5)
    minimo = min (a,b,c)
    return minimo