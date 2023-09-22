def conta_numero(numero,matriz):
    '''Funcao que, dado uma matriz e um numero inteiro,
    retorna quantas vezes aquele numero aparece na matriz
    int, list -> int
    '''
    linha = len(matriz)
    coluna = len(matriz[0])
    for x in range(linha):
        for y in range(coluna):
            if numero == y:
                r += 1
    return r