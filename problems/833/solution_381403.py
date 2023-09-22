def conta_numero(numero,matriz):
    '''retorna quantas vezes um numero aparece na matriz
    int,list(list) -> int'''
    if numero in matriz:
        return list.count(matriz,numero)
    else:
        return 0