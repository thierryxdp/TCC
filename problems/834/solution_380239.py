def media_matriz(mat):
    soma=0
    tamanho=0
    for linha in mat:
        soma+=sum(linha)
        tamanho+=len(linha)
    return round(soma/tamanho,2)