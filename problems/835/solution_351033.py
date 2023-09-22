def melhor_volta(matriz):
    """dado uma matriz 6x10 com os tempos em segundos dos corredores em cada volta,
    a função retornará uma tupla informando de quem foi a melhor volta, com qual tempo
    e em que volta;
    list(list)->tup"""
    corredores=len(matriz)
    A=[]
    corredor=1
    for i in range(corredores):
        list.append(A,[corredor,min(matriz[i]),(list.index((matriz[i]),min(matriz[i]))+1)])
        corredor=corredor+1        
    B=min(A[0][1],A[1][1],A[2][1],A[3][1],A[4][1],A[5][1])
    lista_nova=[]
    for x in range(len(A)):
        for j in range(len(A[0])):
            if B==A[x][j]:
                list.append(lista_nova,A[x])
            
    return(lista_nova[0][0],B,lista_nova[0][2])