def conta_numero(numero,matriz):
    '''dado um numero inteiro e uma matriz de inteiros de qualquer tamanho, retorna quantas vezes aquele numero aparece na matriz. int,lista->int'''
    contador=0
    for i in range(len(matriz)):
        for j in matriz[i]:
            if j==numero:
                contador=contador+1
    return contador