def busca(setor, matriz):
    """Retorne os dados dos funcionários do setor"""
    i = []
    for x in range(len(matriz)):
        if setor == matriz[x][2]:
            i = i + [[matriz[x][0],matriz[x][1]]]
    return i