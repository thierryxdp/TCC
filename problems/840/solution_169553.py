def bolos(A, B, C):
    '''Calcula a quantidade de ovos que joão pode fazer. '''
    farinha=A//2
    ovos=B//3
    leite=C//5
    return min(farinha,ovos,leite)