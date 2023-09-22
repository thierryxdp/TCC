def media_matriz(mat):
    i=0
    cont=0
    for v in mat:
        for numero in v:
            i=i+numero
            cont=cont+1
    return i//cont