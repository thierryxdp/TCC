def media_matriz(matriz:List):
    '''Função quecalcula a média de todos os numeros de uma matriz.
    list->int'''
    tamanho=0
    soma=0
    for linha in matriz:
        tamanho+=len(linha)
        soma+=sum(linha)
    return round(soma/tamanho,2)