def busca(setor,matriz):
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            lista1 = matriz[i]
            lista1.remove(setor)
            if setor in matriz[i][j]:
                lista.append(lista1)
    return lista