def melhor_volta(matriz:list)->tuple:
    """A função recebe como entrada uma matriz 6X10 com os tempos em segundos dos corredores em cada volta.Cada linha representa um jogador, e cada coluna um determinado número de voltas. A função retorna de quem foi a melhor volta, com qual tempo, e em que volta ocorreu"""
    nlin = len(matriz)
    ncol = (len(matriz[0]))
    tempos = []
    matriz_copia = list.copy(matriz)
    for i in range(nlin):
        for j in range(ncol):
            list.append(tempos, matriz[i][j])
    tempo = min(tempos)
    indice = 0
    volta = 0
    while indice < nlin:
        if tempo in matriz[indice]:
            volta = list.index(matriz[indice],tempo) + 1
        else:
            volta = volta
        indice += 1
    jogador = list.index(matriz_copia,tempo)
    return jogador