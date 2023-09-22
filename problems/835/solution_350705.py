def melhor_volta(matriz):
    """dado uma matriz 6x10 com os tempos em segundos dos corredores em cada volta,
    a função retornará uma tupla informando de quem foi a melhor volta, com qual tempo
    e em que volta;
    list(list)->tup"""
    corredores=len(matriz)
    A=[]
    corredor=1
    indice=0
    for i in range(corredores):
        list.append(A,[corredor,min(matriz[i]),(list.index((matriz[i]),min(matriz[i]))+1)])
        corredor=corredor+1        
    B=min(A[0][1],A[1][1],A[2][1],A[3][1],A[4][1],A[5][1])
    indice=0 
    for x in range (len(A)):
        for j in range (x):
            if B==A[x][j]:
                indice=x
    return(A[indice][0],B,A[indice][2])