def media_matriz(matriz):
    '''dada uma matriz de inteiros não vazia (matriz), retorna a média de todos os números da matriz; list -> float'''

    cont = 0
    soma = 0

    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            cont = cont + 1
            soma = soma + matriz[i][j]

    return round(soma/cont,2)