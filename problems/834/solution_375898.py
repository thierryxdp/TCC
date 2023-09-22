def media_matriz(mat):
    '''função chamada que dada uma matriz de inteiros não vazia, retorna a média
       de todos os números da matriz (com exatamente duas casas decimais de precis˜ao).
       list->float '''
    linhas=len(mat)
    colunas=len(mat[0])
    soma=0
    qnt=0
    for i in range(linhas):
        for j in range(colunas):
            soma=soma+mat[i][j]
            qnt=qnt+1
        media=soma/qnt
    return round(media,2)