def media_matriz(A):
    '''funcao que, dada uma matriz A de inteiros nao vazia, retorna a media de todos os
    numeros da matriz com duas casas decimais de precisao;
    matriz -> float'''
    soma=0
    nLinhasA=len(A)
    nColunasA=len(A[0])
    tamanho=nLinhasA*nColunasA
    for i in range(nLinhasA):
        linha=[0]*nColunasA
        list.append(linha,1)
        for j in range(nColunasA):
            soma+=A[i][j]
    return round(soma/tamanho,2)