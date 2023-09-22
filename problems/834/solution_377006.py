def media_matriz(matriz):
    "Retorna a média de todos os números da matriz. matriz->float"
    matriz_soma = []
    quantidade_de_linhas = len(matriz) 
    quantidade_de_colunas = len(matriz[0]) 
    for posicao_linha in range(quantidade_de_linhas):
        linha_da_soma = []
        for posicao_coluna in range(quantidade_de_colunas):
            elemento_da_soma = matriz[posicao_linha][posicao_coluna]
            list.append(linha_da_soma, elemento_da_soma)
        list.append(matriz_soma, linha_da_soma)
        tot = matriz_soma[:]/len(matriz_soma[:])
    return round(tot, 2)