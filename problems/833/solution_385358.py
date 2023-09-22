def conta_numero(numero, matriz):
    '''Retorna quantas vezes o numero
    dado aparece na matriz
    int, list --> int'''
    qntd = 0
    for i in matriz:
        for j in matriz[i]:
            if j == numero:
                qntd += numero
    return qntd