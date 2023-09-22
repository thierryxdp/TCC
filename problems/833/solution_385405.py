def conta_numero(numero, matriz):
    """ dado um numero inteiro e uma matriz, identifica quantas vezes o numero aparece na matriz;
    int,lista->int"""
    p=0
    aux=0
    while p<len(matriz):
        aux+=list.count(matriz[p],numero)
        p+=1
    return aux