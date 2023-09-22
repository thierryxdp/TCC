def conta_numero(numero,matriz):
    '''Dado um número inteiro e uma matriz de inteiros de tamanho
    qualquer, retorna quantas vezes aquele número aparece na matriz
    int,mat->int'''
    qtd=0
    for lin in matriz:
        for elemento in lin:
            if elemento==numero:
                qtd=qtd+1
    return qtd