def conta_numero(numero,matriz):
    
# A função recebe um número inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna
# quantas vezes aquele número aparece na matriz.
# int,list->int

    n_vezes=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                n_vezes = n_vezes+1
    return n_vezes