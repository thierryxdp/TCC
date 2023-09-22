def conta_numero(numero,matriz):
    '''Função que recebe um número int e uma matriz de int;
    conta e retorna quantas vezes o número aparece na matriz.
    int,matriz->int'''
    r = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                r.append(numero)
    return len(r)