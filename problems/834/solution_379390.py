def media_matriz(matriz):
    '''dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz (com exatamente duas casas decimais de precisão)
    list->float
    teste: media_matriz([[7, 1, 2], [8, 2, 4], [2, 4, 6], [5, 1, 3]]) -> 3.75''''
    soma=0
    total_numero=0
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            soma=soma+matriz[i][j]
            total_numero+=1
    media=soma/total_numero 
    return round(media,2)