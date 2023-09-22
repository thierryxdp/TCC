def media_matriz(matriz):
    '''Essa função dada uma matriz de inteiros não vazia como valor de entrada,retorna a média de todos os número da matriz'''
    '''dic -> flot'''
    soma=0
    tamanho=0
    for linha in matriz:
        soma+=sum(linha)
        tamanho+=len(linha)
    return round(soma/tamanho,2)