def melhor_volta(M):
    '''Funcao que recebe uma matriz M(6,10)   
    e obtém o menor tempo, em segundos,
    entre seus elementos.
    list([int]) -> tup(int,int,int)'''    
    linhas=6
    colunas=10
    melhor_volta=1000
    for i in range(linhas):
        for j in range(colunas):
            volta=M[i][j]
            if volta<min(volta,melhor_volta):
                melhor_volta=volta
                melhor_piloto=i-1
                ordinal_volta=j-1
    A=(i,M[i][j],j)
    return A