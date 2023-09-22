def conta_numero(numero,matriz):
    '''a funcao retorna quantas vezes o numero aparece na matriz
    int, list -> int'''
    contagem=0
    for i in range(len(matriz)):
        for j in range (len(matriz[0])):
                        if numero in matriz:
                        contagem=1+ contagem
    return contagem