def bolos(a,b,c):
    '''funcao que retorna o numero de bolos que podem ser feitos em funcao da quantidade de ingredientes.'''
    return min(a//2,b//3,c//5)