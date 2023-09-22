def media_matriz(x):
    ''''''
    soma=0
    tamanho=0
    for linha in x:
        soma+=sum(linha)
        tamanho+=len(linha)
    return round(soma/tamanho,2)