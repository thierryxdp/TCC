def conta_numero (inteiro, matriz):
    '''Função que conta e retorna quantas vezes o número inteiro 
    aparece na matriz de tamanho qualquer.
    int, lista(lista) -> int'''
    contar= 0
    for ind_linha in range(len(matriz)):
        for ind_coluna in range(len(matriz[ind_linha])):
            if matriz[ind_linha][ind_coluna]==inteiro:
                contar+= 1
            return contar