def melhor_volta(matriz):
    '''Funcao que dado uma lista com os tempos dos corredores,
    retorna uma tupla com o piloto, o melhor tempo e a volta.
    list -> tuple
    '''
    ml = []
    linha = len(matriz)
    coluna = len(matriz[0])
    for x in range(linha):
        for y in range(coluna):
            if type(matriz[x][y]) == int or float:
                ml.append(matriz[x][y])
                m = min(ml)
    for x in range(linha):
        if m in matriz[x]:
            n = x + 1
            i = matriz[x].index(m) + 1
    return (n, m, i)