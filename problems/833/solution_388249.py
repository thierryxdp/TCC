def conta_numero (numero, matriz):
    '''Função que conta e retorna quantas vezes o número inteiro 
    aparece na matriz de tamanho qualquer.
    int, lista(lista) -> int'''
    contador= 0
    for ind_linha in range(0,len(matriz)):
        for ind_coluna in range(0,len(matriz[ind_linha])):
            if matriz[ind_linha][ind_coluna]==numero:
                contadorr+= 1
            return contador