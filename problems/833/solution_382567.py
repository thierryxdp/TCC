def conta_numero(numero,matriz):
    '''Retorna uma matriz de inteiros de
       tamanho qualquer, conta e reconta quantas
       vezes o número de entrada aparece na
       matriz;int,matriz->int'''
    i=len(matriz)-1
    contagem=0
    for e in matriz:
        if numero in matriz[i]:
            contagem+=1
        i-=1
    return contagem