def busca(setor,matriz):
    for i in list(range(len(matriz))):
        lista = []
        for j in list(range(len(matriz[0]))):
            if str(setor) in matriz[i][j]:
                list.append(lista, matriz[i])
    return lista