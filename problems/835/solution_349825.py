def melhor_volta(matriz):
    """Dado uma matriz 6x10 (6 linhas e 10 colunas), na qual cada linha representa
    um corredor, cada coluna, uma volta em uma pista e cada elemento, o tempo da volta,
    retorna o corredor vencedor, o menor tempo e a volta mais rápida:
    list(list)-->tuple"""
    soma_matriz=[]
    indices=[]
    linha_matriz=len(matriz)
    coluna_matriz=len(matriz[0])
    resultado=''
    for i in range(linha_matriz):
        for j in range(coluna_matriz):
            if (matriz[i][j]==min(matriz[i])):
                soma_matriz+=[matriz[i][j]]
                indices+=[[i+1,j+1]]
    resultado=min(soma_matriz)
    i=indices[soma_matriz.index(resultado)][0]
    j=indices[soma_matriz.index(resultado)][1]
    return (i,resultado,j)