def media_matriz(m):
    """funcao que dada uma matriz de inteiros nao vazia retorna a media
       de todos os numeros da matriz com exatamente duas casas decimais de
       precisao

       lista-> float
    """

    nlinhas=len(m)
    ncolunas=len(m[0])

    soma= 0
    elementos=0

    for i in range(nlinhas):
        for j in range(ncolunas):
            soma= soma + m[i][j]
            elementos=elementos=1

    return soma/elementos