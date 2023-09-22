def bolos(a,b,c):
    '''recebe a quantidade de farinha (a), de ovos (b) e de leite (c)
    e retorna a quantidade máxima de bolos que joão consegue fazer'''
    farinha = a//2
    ovos = b//3
    leite = c//5
    return min(farinha,ovos,leite)