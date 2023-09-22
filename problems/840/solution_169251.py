import math
def bolos(a,b,c):
    ''' Calcula o número máximo de bolos que podem ser feitos com os ingredientes dispomiveis,
    dado a quantidade de farinha, ovos e leite disponíveis. '''
   farinha = a//2
   ovos = b//3
   leite = c//5
    return min(farinha, ovos,leite)