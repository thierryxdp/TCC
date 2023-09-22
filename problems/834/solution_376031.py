def media_matriz(mat):
    """Para retornar a média dos números de uma matriz, digite;
    matriz->float"""
    s=0
    t=0
    for Lin in range(len(mat)):
        for Col in range(len(mat[Lin])):
            t+=1
            s+= mat[Lin][Col]
        media=s/t
    return roud(media,2)