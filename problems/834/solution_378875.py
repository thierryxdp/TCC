def media_matriz(matriz):
    """dada uma matriz de números inteiros não vazia, a função retorna a média de todos
    os números da matriz(com exatamente duas casas decimais de precisão);
    list(list)->float"""
    linha=len(matriz)
    coluna=len(matriz[0])
    soma_termos=0
    total_termos=linha*coluna
    for i in range(linha):
        for j in range(coluna):
            soma_termos=soma_termos+matriz[i][j]
    return round((soma_termos/total_termos),2)