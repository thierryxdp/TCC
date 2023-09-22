def busca(setor,matriz):
    lista = []
    matrizes = range(len(matriz))
    for i in matrizes:
        if setor == matriz[i][2]:
            lista= lista + [[matriz[i][0], matriz[i][1], matriz[i][3]]]
    return lista