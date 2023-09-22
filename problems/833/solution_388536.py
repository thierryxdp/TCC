def conta_numero(numero,matriz):
    '''função que dada um numero inteiro e uma matriz de inteiros
       de tamanho qualquer, conta e retorna quantas vezes aquele
       número aparece na matriz;
       int, matriz -> int'''
    s = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                s += 1
            else:
                s += 0
    return s