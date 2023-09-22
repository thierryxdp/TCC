def conta_numero(numero,matriz):
    '''conta quantas vezes um numero aparece em uma matriz
    int,list->int'''
    ocorrencias=0
    for i in len(matriz):
        for j in len(matriz[i]):
            list.count(matriz[i],numero)
            ocorrencias=ocorrencias+1
    return ocorrencias