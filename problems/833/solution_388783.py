def conta_numero(numero,matriz):
    '''Dado um numero inteiro e uma matriz de inteiros, retorna
    quantas vezes aquele numero aparece na matriz'''
    '''int,list->int'''
    vezes=0
    for linha in matriz:
        vezes=vezes+list.count(linha,numero)
    return vezes