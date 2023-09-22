def busca(nome,matriz):
    lista = []
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            if matriz[x][y]==nome:
                lista.append(matriz[x])
    for z in range(len(lista)):
        del lista[z][2]
    return lista