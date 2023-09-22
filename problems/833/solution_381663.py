def conta_numero(num,mat):
    '''funç˜ao que dado um número inteiro e uma matriz de inteiros de
       tamanho qualquer, conta e retorna quantas vezes aquele número aparece
       na matriz. int,list --> int '''
    linhas=len(mat) 
    colunas=len(mat[0])
    qnt=0
    for i in range(linhas):
        for j in range(colunas):
            if mat[i][j]==num:
        qnt=qnt+1
    return qnt