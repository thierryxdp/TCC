def busca(setor,matriz):
    lista = []
    for i in range(len(matriz)):
        lista1 = matriz[i]
        del lista1[2]
        if setor in matriz[i]:
                lista.append(lista1)
    return lista