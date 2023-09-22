def busca(nome,matriz):
    lista = []
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            if matriz[x][y]==nome:
                lista.append(matriz[x][0])
                lista.append(matriz[x][1])
                lista.append(matriz[x][3])
    return lista