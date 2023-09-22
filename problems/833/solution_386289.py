def conta_numero(numero,matriz):
    '''Dado um número inteiro e uma matriz de inteiros de tamanho
    qualquer, retorna quantas vezes aquele número aparece na matriz
    int,mat->int'''
    lin=len(matriz)
    qtd=0
    for elemento in matriz:
        if elemento==numero:
            qtd=qtd+1
    return qtd