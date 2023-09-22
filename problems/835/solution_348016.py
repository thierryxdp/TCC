def melhor_volta(matriz):
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
            nome = matriz[x][0]
            i = matriz[x].index(m)
    return (nome, m, i)