def media_matriz(mat):
    '''função que, dada uma matriz de inteiros não vazia(mat),
    retorna a média de todos os números da matriz com duas casas
    decimais.  list->float'''
    contador=0
    soma=0
    for i in range(len(mat)):
        if len(mat) !=0:
            soma=soma+sum(mat[i])
            contador=contador+len(mat[i])
            media= soma/contador
            resultado= round(media,2)
    return resultado