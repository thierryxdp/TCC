def conta_numero(numero,matriz):
    '''retorna quantas vezes um numero aparece na matriz
    int,list(list) -> int'''
    while numero in matriz:
        return list.count(matriz,numero)
    if numero not in matriz:
        return 0