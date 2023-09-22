def conta_numero(numero,matriz):
    '''dado um número inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna quantas vezes aquele número aparece na matriz
    int,list->int
    teste:conta_numero(9, [[9, 4, 9, 8, 8]])->2''''
    if matriz==[]:
        return 0
    soma=0
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j]==numero:
                soma+=1
    return soma