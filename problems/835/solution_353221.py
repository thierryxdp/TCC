def melhor_volta(M6x10):
    '''
    dado uma matriz 6x4 como entrada, retorna uma tupla
    com 3 elementos: a linha onde se encontra o menor elemento,
    o menor elemento e em qual coluna se encontra o menor 
    elemento
    dados de entrada: list
    retorna: tuple
    '''
    acumulador = []
    menor_tempo = [M6x10[0][0]]
    for i in range(6):
        for j in range(10):
            list.append(acumulador,(i+1,M6x10[i][j],j+1))
    for k in range(len(acumulador)):
        menor_tempo[0] = min(acumulador[k][1],menor_tempo[0])
        if acumulador[k][1] in menor_tempo:
            posicao = k
    return acumulador[k]