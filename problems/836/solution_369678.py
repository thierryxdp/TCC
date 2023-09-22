def busca(setor,matriz):
    lista = []
    for i in list(range(len(matriz))):
        for j in list(range(len(matriz[0]))):
            if setor in matriz[i][j]:
                list.append(lista, matriz[i])
    for a in list(range(len(lista))):
        for b in list(range(len(lista[0]))):
            del lista[a][2]
    return lista