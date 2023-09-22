def melhor_volta(M):
    '''Funcao que recebe uma matriz M(6,10)   
    e obtém o menor tempo, em segundos,
    entre seus elementos.
    list([int]) -> tup(int,int,int)'''    
    linhas=6
    colunas=10
    melhor_volta=1000
    melhor_piloto=0
    ordinal_volta=0
    for i in range(linhas):
        for j in range(colunas):
            volta=M[i][j]
            minimo=min(volta,melhor_volta)
            if volta==minimo:
                melhor_volta=volta
                melhor_piloto=i+1
                ordinal_volta=j+1
    A=(melhor_piloto,melhor_volta,ordinal_volta)
    return A