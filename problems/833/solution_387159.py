def conta_numero(numero, matriz):
    '''Dado um numero inteiro e uma matriz de inteiros, conta e retorna quantas vezes 
    aquele numero aparece na matriz;
    list -> int'''

    cont = 0

    for i in range(len(matriz)):
        cont += list.count(matriz[i], numero)

    return cont