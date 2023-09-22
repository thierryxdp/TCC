def conta_numero(numero,matriz):
    '''dado um numero e uma matriz,
    conta quantas vezes esse numero aparece na matriz
    entra: in,lista
    sai:int'''
    p=0
    for i in matriz:
        for k in i:
            if numero==k:
                p+=1
    return p