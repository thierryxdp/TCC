def busca(setor,matriz):
    lista = []
    for i in range(len(matriz)):
        if setor in matriz[i][2]:
            del matriz[i][2]
            list.append(lista,matriz[i])
    return lista