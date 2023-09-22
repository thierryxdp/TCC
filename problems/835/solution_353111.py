def melhor_volta(matriz610):
    '''retorna a volta mais rapida da corrida
    list(list) -> int'''
    tempos_de_voltas = ()
    for i in range(len(matriz610)):
        for j in range(len(matriz610[i])):
            tempos_de_voltas += matriz610[i][j]
            maisrapido = min(tempos_de_voltas)
    return tempos_de_voltas