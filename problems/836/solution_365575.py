def busca(setor, matriz):

    lista = []

    for l in range(0,3):
        if setor in matriz[l]:
            lista.append(matriz[l])

    return lista