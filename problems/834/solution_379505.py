def media_matriz(x):
    soma=0
    tamanho=0
    for linha in x:
        soma+=sum(linha)
        tamanh0+=len(linha)
    return round(soma/tamanho,2)