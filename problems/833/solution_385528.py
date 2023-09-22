def conta_numero(numero,matriz):
    '''
       funcao que dado um numero inteiro e uma matriz de
       inteiros, retorna quantas vezes o numero aparece
       na matriz
       int, list -> int
    '''
    if matriz == []:
        return 0
    nlinhas = len(matriz)
    ncolunas = len(matriz[0]) 
    qtd_numero = 0
    for i in range(nlinhas):
        for j in range(ncolunas):
            if matriz[i][j] == numero:
                qtd_numero = qtd_numero + 1 
    return qtd_numero