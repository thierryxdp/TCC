def busca(setor, matriz):
    lista = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            list.append(matriz[i])
    return lista