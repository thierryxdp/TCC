def media_matriz(matriz):
    '''
    função que dada uma matriz de inteiros não vazia, retorna a média de todos os elementos
    da matriz com exatamente duas casas decimais de precisão
    list(list)-->float
    '''
    soma=0
    divisor=0
    media_matriz=0
    for linha in matriz:
        soma= soma+ sum(linha)
        divisor= divisor+ len(linha)
    media_matriz= media_matriz+(soma/divisor)

    return round(media_matriz,2)