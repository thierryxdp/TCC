def busca(setor,matriz):
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            lista1 = matriz[i][j]
            if setor in matriz[i][j]:
                lista1.remove(setor)
                lista.append(lista1)
    return lista