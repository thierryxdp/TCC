def media_matriz(matriz):
    '''função que ao dar uma matriz de numeros inteiros não
       vazios retorna a média de todos os números da matriz
       com 2 casas decimais de precisão
       list(list) ---> float '''
    linhas = len(matriz)
    soma = 0
    tamanho = 0
    b = 0
    for a in range(linhas):
        colunas = len(matriz[0])
        tamanho = linhas * colunas
        while b < len(colunas):
            soma = soma + matriz[a][b]
            b += 1
    divisao = soma/tamanho
    return round(divisao, 2)