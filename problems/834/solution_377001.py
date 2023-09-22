def media_matriz(matriz):
    ''' Funcao que dada uma matriz, retorna a media de todosos
    numeros da matriz'''
    soma=0
    tamanho=0
    for linha in matriz:
        soma+= sum(linha)
        tamanho+= len(linha)
    return soma/tamanho