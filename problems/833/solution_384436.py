def conta_numero(matriz, inteiro):
    '''conta o numero de vezes que o numero inteiro apareceu na matriz dada;
    list(list)-> int'''

    repetidos=[]
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if matriz[l][c] == inteiro:
                list.append(repetidos,inteiro)
    return len(repetidos)