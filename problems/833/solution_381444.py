def conta_numero(n,matriz):
    '''Retorna quantas vezes o número n aparece na matriz dada'''
    '''int,list->int'''
    vezes=0
    for i in range(len(matriz)):
        vezes+=list.count(matriz[i],n)
    return vezes