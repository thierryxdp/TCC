def melhor_volta(matriz):
    mst=[]
    for c in range(len(matriz)):
        mst+=[min(matriz[c])]
    mt=min(mst)
    corredor=(mst.index(mt)+1)
    volta=((matriz[corredor]).index(mt)+1)
    return (corredor,mt,volta)