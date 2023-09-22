def conta_numero(numero,matriz):
    '''Recebe um numero inteiro e uma matriz e retona quantas vezes o numero aparece na matriz
    int,matriz -> int'''
    total=0
    for lista in matriz:
        for elem in lista:
            if elem==numero:
                total=total+1
    return total