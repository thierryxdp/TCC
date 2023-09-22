def melhor_volta(matriz:list)->tuple:
    """  A função recebe como entrada uma matriz 6X10 com os tempos em segundos dos corredores em cada volta.Cada linha representa um jogador, e cada coluna um determinado número de voltas. A função retorna de quem foi a melhor volta, com qual tempo, e em que volta ocorreu"""
    nlin = len(matriz)
    ncol = (len(matriz[0]))
    tempos = []
    for i in range(nlin):
        tempo = []
        for j in range(ncol):
            list.append(tempo, matriz[i][j])
        list.append(tempos,tempo)   
    
    
    tempo = min(tempos)
    return tempos