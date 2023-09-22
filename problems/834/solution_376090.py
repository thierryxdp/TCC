def media_matriz(matriz):
    '''função que dada uma matriz de inteiros não vazia, retorna a média de todos os núemeros da matriz com
    precisão de duas casas decimais.
    list -> float'''
    
    for i in range(len(matriz)):
        soma = 0
        for n in range(len(matriz[i])):
            soma = soma + matriz[i][n]
    return soma