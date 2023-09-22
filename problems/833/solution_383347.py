def conta_numero(numero, matriz):
    '''função que dada uma matriz e um número retorna quantas vezes
    o número aparece na matriz'''
    coluna = len(matriz)
    linha = len(matriz[0])
    contador = 0
    for i in coluna:      
        for j in linha:
                if numero in matriz[j]:
                    contador = contador + 1
    return contador