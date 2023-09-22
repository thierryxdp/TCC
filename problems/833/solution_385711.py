def conta_numero(numero,matriz):
    '''conta quantas vezes o numero dado aparece na matriz;
    int/matriz->int'''
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                soma=soma+1
    return soma