def media_matriz(m):
    """Dada uma matriz de números inteiros não vazia
    retorna a média de todos os números com 2 casas decimais 
    de precisão
    list-->float"""
    soma=0
    for linha in m:
        for n in linha:
            soma=soma+n
    media=soma/(len(m)*len(m[0]))
    return media