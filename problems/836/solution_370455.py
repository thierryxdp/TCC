def busca(setor, matriz):
    lista = []

    for i in range(len(matriz)):
        if setor in matriz[i]:
            lista.append(matriz[i])

    for j in range(len(lista)):
        lista[j].remove(setor)

    return lista