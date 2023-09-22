def melhor_volta(matriz):
    """..."""
    lista = [0,0,0]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            minimo = min(matriz[i])
            if matriz[i][j] == minimo:
                list[0] = i+1
                list[1] = matriz[i][j]
                list.append = j+1
    return tuple(lista)