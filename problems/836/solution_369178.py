def busca(setor,matriz):
    lista_nova = []
    for i in range(len(matriz)):
        if matriz[i][2] in setor:
            lista_nova.append(matriz[i][0])
            lista_nova.append(matriz[i][1])
            lista_nova.append(matriz[i][2])
    return lista_nova