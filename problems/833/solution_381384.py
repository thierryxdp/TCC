def conta_numero(numero,matriz):
    '''conta quantas vezes um numero aparece em uma matriz
    int,list->int'''
    ocorrencias=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.count(matriz[i],numero)
            ocorrencias=ocorrencias+1
    return ocorrencias