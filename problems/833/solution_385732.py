def conta_numero(num,A):
    '''funcao que, dado um numero inteiro e uma matriz, retorna a
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