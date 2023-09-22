def media_matriz(x):
    '''função que dada uma matriz não vazia retorna a média; dic => flot'''
    soma=0
    tamanho=0
    for linha in x:
        soma+=sum(linha)
        tamanho+=len(linha)
    return round(soma/tamanho,2)