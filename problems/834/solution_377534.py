def media_matriz(m):
    ''' Dada uma matriz de inteiros nao vazia, retorna a media
    de todos os numeros da matriz. list--> float '''
    
    for i in (len (m)):
        for j in (len (m[0])):
            soma_col += m[i][j]
    num = len (m[0]) * len (m)
    media = round(soma_col/num , 2)
    return media