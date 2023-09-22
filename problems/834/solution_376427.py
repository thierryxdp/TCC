def media_matriz(m):
    """Recebe uma matriz de inteiros não vazia,calcula e retorna a média de todos os números da matriz com exatamente duas casas decimais de precisão;list->float"""
    s=0
    for lista in m:
        s=s+sum(lista)
    return round(s/(len(m)*len(m[0])),2)