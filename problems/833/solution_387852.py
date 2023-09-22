def conta_numero(n,matriz):
    ''' Função que recebe um interio qualquer e uma matriz, e retorna
    quantas vezes aquele inteiro aparece dentro da matriz
    int, list -> int '''

    i=0
    ocorrencias = 0
    for elem in matriz:
        if n in matriz[i][i]:
             ocorrencias = ocorrencias + 1
        i = i+1
    return ocorrencias