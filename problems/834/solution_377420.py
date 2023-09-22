def media_matriz(mat):
    '''Função que recebe uma matriz(mat) de números int;
calcula e retorna a média de todos os números da matriz.
matriz->float'''
    s = 0
    t = 0
    for l in mat:
        s = s+sum(l)
        t =t+len(l)
    return round(s/t,2)