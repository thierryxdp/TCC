def conta_numero(numero,matriz):
    '''a funcao retorna quantas vezes o numero aparece na matriz
    int, list -> int'''
    for i in range(len(matriz)):
        for j in range (len(matriz[0])):
                        if numero in matriz:
                        contagem= contagem+1
    return contagem