def media_matriz(mat):
    '''Dada uma matriz é retornada a media dos valores
    dessa matriz arredondados para duas casas decimais
    list---->float'''
    soma = 0
    for linha in mat:
        for coluna in linha:
            soma += coluna
    media = soma/(len(mat)*len(mat[0]))
    return round(media,2)