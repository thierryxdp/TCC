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
    for i in range(6):
        for j in range(10):
            list.append(acumulador,M6x10[i][j])
        menor_tempo = min(acumulador)
        for i in range(6):
            for j in range(10):
                if menor_tempo == M6x10[i][j]:
                    return (i + 1, menor_tempo, j+1)