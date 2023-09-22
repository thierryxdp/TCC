def conta_numero(numero,matriz):
    """ Dada uma mtariz e um número, conta quantas vezes esse número aparece na matriz:
    int,list->int """
    quantidade=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                quantidade+=1

    return quantidade