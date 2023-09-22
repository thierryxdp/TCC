def conta_numero (numero,matriz):
    '''funçao que dado um numero inteiro
    e uma matriz de inteiros conta
    e retorna quantas vezes aquele
    numero aparece na matriz.
    int,list->int'''
    x=0
    for linha in matriz:
        x=x+list.count(linha,numero)
    return m