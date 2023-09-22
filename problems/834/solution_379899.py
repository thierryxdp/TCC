def media_matriz(mat):
    """retorna a media dos numeros de uma matriz; list->float"""
    qtd=0
    soma=0
    for i in range(mat):
        for j in range(mat[0]):
            soma+=mat[i][j]
            qtd+=1
    return round(soma/qtd,2)