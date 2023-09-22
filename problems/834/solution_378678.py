def media_matriz(matriz):
    """Função que dada uma matriz de inteiros não vazia,
       retorna a média de todos os números da matriz(com
       exatamente duas casas de precisão);
       list(list) -> float"""
    soma_elementos = 0
    linhas = len(matriz)
    colunas = len(matriz[0])
    numero_elementos = linhas * colunas 
    for i in range(len(linhas)):
        for j in range(len(colunas)):
            soma_elementos = soma_elementos + matriz[i][j]
    media = soma_elementos/numero_elementos
    return media