def busca(matriz, setor):
    '''b'''
    registros = []
    linha = len(matriz)
    for i in range(linha):
        if setor == matriz[i][2]:
            registros += matriz[i][0],matriz[i][1],matriz[i][3]
    return registros