def busca(setor,matriz):
    lista = []
    for i in range(len(matriz)):
        lista1 = matriz[i]
        del lista1[2]
        for j in range(len(matriz[i])):
            if setor in matriz[i][j]:
                lista.append(lista1)
    return lista