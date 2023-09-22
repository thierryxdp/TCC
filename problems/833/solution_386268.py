def conta_numero(numero,matriz):
    '''Dado um número inteiro e uma matriz de inteiros de tamanho
    qualquer, retorna quantas vezes aquele número aparece na matriz
    int,mat->int'''
    lin=len(matriz)
    col=len(matriz[0])
    qtd=list.count(matriz,numero)
    return qtd