def melhor_volta(matriz: list)-> tuple:
    """Dada uma matriz 6x10 (10 voltas para cada um dos 6 corredores)com os
    tempos em segundos dos corredores em cada volta. A função retorna uma
    tupla contendo: de quem foi a melhor volta, com qual tempo e em que volta"""
    numlinhas = len(matriz)
    numcolunas = len(matriz[0])
    for i in range(numlinhas):
        for j in range(numcolunas):
            tempo = min(lista)
    for i in range(numlinhas):
        if tempo in matriz[i]:
            corredor = i+1
        for j in range(numcolunas):
            if matriz[i][j] == tempo:
                volta = j+1
    return tuple(corredor, tempo, volta)