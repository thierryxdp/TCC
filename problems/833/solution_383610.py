def conta_numero(numero,matriz):
    '''função que, dado um número inteiro e uma matriz de inteiros, conta 
    e retorna quantas vezes aquele nuemro aparece na matriz.
    int, list -> int'''
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    quantas_vezes = 0
    
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == numero:
                quantas_vezes += 1
    return quantas_vezes