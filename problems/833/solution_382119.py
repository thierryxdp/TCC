def conta_numero (numero, matriz):
    '''Funcao que, dado um numero e uma matriz, conta e retorna quantas vezes esse numero aparece na matriz.
    int, list -> int'''
    
    if numero in matriz:
        return matriz.count(numero)