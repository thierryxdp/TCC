def busca(matriz, setor):
    '''b'''
    registros = []
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            if setor == matriz[i][j=2]:
                registros += matriz[i][j=0],matriz[i][j=1],matriz[i][j=3]
    return registros