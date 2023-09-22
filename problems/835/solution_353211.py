def melhor_volta(M6x10):
    '''
    dado uma matriz 6x4 como entrada, retorna uma tupla
    com 3 elementos: a linha onde se encontra o menor elemento,
    o menor elemento e em qual coluna se encontra o menor 
    elemento
    dados de entrada: list
    retorna: tuple
    '''
    acumulador_tempo = [99999999999999999999999999999999999]
    acumulador_corredor = []
    acumulador_volta = []
    for i in range(6):
        for j in range(10):
            if M6x10[i][j] < acumulador_tempo[0]:
                acumulador_tempo = M6x10[i][j]
                acumulador_corredor = [i + 1]
                acumulador_volta = [j + 1]
    return (acumulador_corredor[0],acumulador[0],acumulador_volta[0])