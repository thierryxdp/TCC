def conta_numero(A,num):
    '''funcao que, dada uma matriz e um numero inteiro, retorna a
    quantidade de ocorrencias desse numero na matriz;
    matriz, int -> int'''
    ocorrencias=0
    nLinhasA=len(A)
    nColunasA=len(A[0])
    for i in range(nLinhasA):
        linha=[0]*nColunasA
        list.append(linha,1)
        for j in range(nColunasA):
            if A[i][j]==num:
                ocorrencias += 1
    return ocorrencias