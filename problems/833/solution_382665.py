def conta_numero(numero,matriz):
    lista = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                lista = lista + 1
            return lista
    else:
        return 0