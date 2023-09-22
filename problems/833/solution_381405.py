def conta_numero(numero,matriz):
    '''retorna quantas vezes um numero aparece na matriz
    int,list(list) -> int'''
    for numero in matriz:
        if numero not in matriz:
            return 0
        else:
            return list.count(matriz,numero)