def media_matriz(mat):
    soma = 0
    for linha in mat:
        for coluna in linha:
            soma += coluna
    media = soma/(len(mat)*len(mat[0]))
    return media