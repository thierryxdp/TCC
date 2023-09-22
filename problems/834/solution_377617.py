def media_matriz(matriz):
    """função que dada uma matriz de número inteiro não vazia, retorna a média de todos os números da matriz, com exatamente duas casas decimais;list-->float"""
    soma=0
    for linha in matriz:
        soma=soma+sum(linha)
        media=soma/(len(matriz)*len(matriz[0]))
    return round(media,0)