def melhor_volta(matriz):
    mst=[]
    for c in range(len(matriz)):
        mst+=[min(matriz[c])]
    mt=min(mst)
    Icorredor=(mst.index(mt))
    volta=(matriz[Icorredor].index(mt)+1)
    corredor=Icorredor+1
    
    return (corredor,mt,volta)