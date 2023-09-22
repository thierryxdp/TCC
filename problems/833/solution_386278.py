def conta_numero(numero,matriz):
    '''Dado um número inteiro e uma matriz de inteiros de tamanho
    qualquer, retorna quantas vezes aquele número aparece na matriz
    int,mat->int'''
    lin=len(matriz)
    qtd=0
    i=0
    while i<=lin:
        qtd=qtd+list.count(matriz[i],numero)
        i=i+1
    return qtd