def media_matriz(matriz):
    ''' função que dada uma matriz de inteiros nao vazia, retorna a media de todos os numeros da matriz'''
    soma=0
    tamanho=0
    for linha in matriz:
        soma+=sum(linha)
        tamanho+=len(linha)
    return round(soma/tamanho,2)