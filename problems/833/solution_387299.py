def conta_numero(numero,matriz):
    '''retorna quantas vezes o numero aparece na matriz
    int,matriz->int'''
    a=0
    for i in range(len(matriz)):
        if numero in matriz[i]:
            a+=1
    return a