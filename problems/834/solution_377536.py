def media_matriz(m):
    ''' Dada uma matriz de inteiros nao vazia, retorna a media
    de todos os numeros da matriz. list--> float '''
  
	soma_col = 0

    for i in range(len (m)):
        for j in range(len (m[0])):
            soma_col += m[i][j]
    num = len (m[0]) * len (m)
    media = round(soma_col/num , 2)
    return media