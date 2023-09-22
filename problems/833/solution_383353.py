def conta_numero(numero, matriz):
    '''função que dada uma matriz e um número retorna quantas vezes
    o número aparece na matriz'''
    if matriz != []:
    	linha = len(matriz)
    	coluna = len(matriz[0])
    igual = 0
    for i in range(linha):
        contador = 0
        while contador < coluna:
                if matriz[i][contador] == numero:
                    igual = igual + 1
                contador = contador + 1
    return igual