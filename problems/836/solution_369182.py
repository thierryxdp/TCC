def busca(setor,matriz):
    lista_nova = []
    for i in range(len(matriz)):
        if matriz[i][2] in setor:
            lista_nova.append(matriz[0])
            lista_nova.append(matriz[1])
            lista_nova.append(matriz[3])
    return lista_nova