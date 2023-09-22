def media_matriz(m):
    """Recebe uma matriz de inteiros não vazia,calcula e retorna a média de todos os números da matriz com exatamente duas casas decimais de precisão;list->float"""
    for lista in m:
        s=sum(lista)
    return s/(len(m)*len(m[0]))