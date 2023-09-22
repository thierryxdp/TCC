def media_matriz(matriz:List):
    tamanho=0
    soma=0
    for linha in matriz:
        tamanho+=len(linha)
        soma+=sum(linha)
    return round(soma/tamanho,2)