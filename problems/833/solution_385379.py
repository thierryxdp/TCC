def conta_numero(valor,matriz):
    '''Dado um numero e uma matriz, a função
    calculará a quantidade de vezes em que esse
    numero aparece na matriz. int,list->int'''
    mostragem=0   
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if valor== matriz[i][j]:
                mostragem=mostragem+1
    return mostragem