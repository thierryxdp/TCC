def busca(setor,matriz):
    lista = []
    matrizes = range(len(matriz))
    for i in matrizes:
        if setor == matriz[i][2]:
            lista = list.append(lista,matriz[i])
    return lista