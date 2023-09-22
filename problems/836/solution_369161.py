def busca(setor,matriz):
    lista_nova = []
    for i in range(len(matriz)):
        if matriz[i][2] in setor:
            lista_nova.append(matriz[i][0],matriz[i][1],matriz[i][3])
    return lista_nova