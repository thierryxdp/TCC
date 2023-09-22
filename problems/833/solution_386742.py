def conta_numero(numero, matriz):
    '''Verifico se dado numero existe na matriz e se existir conta quantas vezes ele se repete nesta lista.
int,list->int'''
    ret = 0
    for l in range(0, len(matriz)):
        for c in range(0, len(matriz[l])):
            if matriz[l][c] == numero:
                ret += 1
    return ret