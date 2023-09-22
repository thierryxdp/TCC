def busca(setor, matriz):
    lista = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            matriz[i].pop(2)
            lista.append(matriz[i])
        else:
            pass
    return lista