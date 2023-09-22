def busca(setor, matriz):
    lista = []
    for i in list(range(len(matriz))):
        for j in list(range(len(matriz[0]))):
            if setor in matriz[i][j]:
                list.append(lista, matriz[i])
                list.remove(lista, setor)
    return lista