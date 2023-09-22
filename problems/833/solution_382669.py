def conta_numero(numero,matriz):
    '''Conta e retorna quantas vezes determinado numero aparece em uma matriz'''
    lista = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                lista = lista + 1
    return lista