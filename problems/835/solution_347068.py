def melhor_volta(matriz):
    """..."""
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            minimo = min(matriz[i][j])
            if matriz[i][j] == minimo:
                list.append(lista,i+1)
                list.append(lista,matriz[i][j])
                list.append(lista,j+1)
    return tuple(lista)