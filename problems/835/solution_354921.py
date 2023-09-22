def melhor_volta(matriz):
    '''dada uma matriz com corredores e seus tempos em cada volta, e retorna uma tupla com o melhor corredor, seu tempo e em qual volta; list -> tup'''
    tempos = []
    for linha in matriz:
        for tempo in linha:
            tempos += [tempo]
    tempo_min = min(tempos)
    corredor = 1
    volta = 1
    for linha in matriz:
        if tempo_min in linha:
            corredor += list.index(matriz,linha)
            volta += list.index(linha,tempo_min)
    return (corredor,tempo_min,volta)