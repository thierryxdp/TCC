def busca(setor,matriz):
    lista = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            del matriz[i][2]
            lista.append(matriz[i])
    return lista