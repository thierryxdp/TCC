def melhor_volta(matriz):
    corredores = len(matriz)
    A= []
    corredor = 1
    for i in range(corredores):
        list.append(A,[corredor,min(matriz[i]),(list.index((matriz[i]),min(matriz[i])))])
        corredor += 1
    B = min(A[0][1],A[1][1],A[2][1],A[3][1],A[4][1],A[5][1])
    lista_nova = []
    for x in range(len(A)):
        if B==A[x][1]:
            indice = x
            list.append(lista_nova,A[indice])
    return(lista_nova[0][0],B,lista_nova[0][2])