def melhor_volta(matriz):
    """
    recebe uma matriz 6x10 com os 10 tempos dos 6 corredores
    e retorna uma tupla com o corredor o tempo e o numero da volta
    da melhor volta .
    """
    t1=min(matriz[0])
    i1=list.index(matriz[0],t1)
    t2=min(matriz[1])
    i2=list.index(matriz[1],t2)
    t3=min(matriz[2])
    i3=list.index(matriz[2],t3)
    t4=min(matriz[3])
    i4=list.index(matriz[3],t4)
    t5=min(matriz[4])
    i5=list.index(matriz[4],t5)
    t6=min(matriz[5])
    i6=list.index(matriz[5],t6)
    
    menortempo=min(t1,t2,t3,t4,t5,t6)
    
    if menortempo==t1:
        return (1,t1,i1)
    if menortempo==t2:
        return (2,t2,i2)
    if menortempo==t3:
        return (3,t3,i3)
    if menortempo==t4:
        return (4,t4,i4)
    if menortempo==t5:
        return (5,t5,i5)
    if menortempo==t6:
        return (6,t6,i6)