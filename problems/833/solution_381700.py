def conta_numero2(num,mat):
    '''funç˜ao que dado um número inteiro e uma matriz de inteiros de
       tamanho qualquer, conta e retorna quantas vezes aquele número aparece
       na matriz. int,list --> int '''
    linhas=len(mat) 
    colunas=len(mat[0])
    mat=str(mat)
    num=str(num)
    for i in range(linhas):
        for j in range(colunas):
            qnt=str.count(mat,num)
    return qnt