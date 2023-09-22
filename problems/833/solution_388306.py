def conta_numero(n,matriz):
    ''' Função que recebe um interio qualquer e uma matriz, e retorna
    quantas vezes aquele inteiro aparece dentro da matriz
    int, list -> int '''


    ocorrencias = 0
    for linha in matriz:
        for coluna in matriz:
            if n == coluna:
                ocorrencias = ocorrencias + 1
  
    return ocorrencias