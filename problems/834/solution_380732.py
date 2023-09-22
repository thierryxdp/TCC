def media_matriz(mat):
    """A função que recebe uma matriz de inteiros e retorna
    a média de todos os números que a compõe"""
    tot_elementos= len(mat)*len(mat[0]) #linhas x colunas = número de elementos
    soma=0
    for linhas in mat:
        soma+=sum(linhas)
    media = (soma)/(tot_elementos)
    return round(media,2)