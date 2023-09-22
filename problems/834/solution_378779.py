def media_matriz(matriz):
    '''Uma função que ao receber uma matriz retorna a media 
    de todos os números de dentro da matriz'''
    soma = 0
    tamanho = 0
    for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)
        somaf =soma/tamanho
        somaf = round(somaf,2)
    return somaf