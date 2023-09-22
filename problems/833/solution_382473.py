def conta_numero(num, matriz):
    '''Dada uma matriz e um numero inteiro, retorna a quantidade de vezes que esse numero aparece na matriz.
    list -> int'''
    cont = 0

    for i in matriz:
        for j in i:
            if j == num:
                cont += 1
    return cont