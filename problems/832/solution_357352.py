def eh_quadrada(matriz):
    '''Funcao que recebe uma matriz e
verifica se esta e quadrada ou nao. Lembrando,
uma matriz sem linha e coluna tambem e considerada
quadrada'''
    if len(matriz)!= 0:
        return len(matriz) == len(matriz[0])
    else:
        return False