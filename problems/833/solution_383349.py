def conta_numero(numero, matriz):
    '''função que dada uma matriz e um número retorna quantas vezes
    o número aparece na matriz'''
    coluna = len(matriz)
    linha = len(matriz[0])
    contador = 0
    for i in range(coluna):      
        for j in range(linha):
                if numero in matriz[i][j]:
                    contador = contador + 1
    return contador