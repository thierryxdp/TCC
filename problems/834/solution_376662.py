def media_matriz(matriz):
    '''Função que recebe uma matriz de inteiros não vazia e retorna a média de
    todos os números da matriz; list -> float'''
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    cont = 0
    soma = 0
    
    for i in range(linhas):
        for j in range(colunas):
            soma += matriz[i][j] 
            cont += 1
    
    return round(soma/cont, 2)