def media_matriz(mat):
    contador=0
    soma=0
    for i in range(len(mat)):
        soma=soma+sum(mat[i])
        contador+contador+len(mat[i])
        media= soma/contador
        resultado= round(media,2)
    return resultado