def melhor_volta(matriz):
    """..."""
    
    lista = [0,0,0]
    
    for i in range(len(matriz)):
        minimo = min(matriz[i])
        for j in range(len(matriz[0])):
            if matriz[i][j] == minimo:
                lista[0] = i+1
                lista[1] = matriz[i][j]
                lista[2] = j+1
    return tuple(lista)