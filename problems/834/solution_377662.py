def media_matriz(mat):
    '''funcao que retorna a media de todos os numeros de
    uma matriz nao vazia; list->float'''
    f=0
    soma=0
    soma2=0
    while f in range (len(mat)):
        soma=soma+len(mat[f])
        f=f+1
    return round(soma2/soma,2)