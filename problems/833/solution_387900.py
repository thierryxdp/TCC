def conta_numero(n,matriz):
    ''' Função que recebe um interio qualquer e uma matriz, e retorna
    quantas vezes aquele inteiro aparece dentro da matriz
    int, list -> int '''

    i=0
    ocorrencias = 0
    for linha in matriz:
        for couna in matriz[i]:
            if n == coluna:
                ocorrencias = ocorrencias + 1
        i = i+1
    return ocorrencias