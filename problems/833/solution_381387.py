def conta_numero(numero,matriz):
    '''conta quantas vezes um numero aparece em uma matriz
    int,list->int'''
    i=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            ocorrencias=list.count(numero,matriz[i])
            i=i+1
            ocorrencias=ocorrencias+1
    return ocorrencias