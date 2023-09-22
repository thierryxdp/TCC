def melhor_volta(matriz):
    'dadas as informações de cada volta de cada corredor, returna uma tupla informando qual foi o corredor mais rapido e em qual volta. list -> tuple'
    melhortempo2=[]
    k=0
    i=0
    while i in range(len(matriz)):
        melhortempo2 = melhortempo2 + [min(matriz[i])]
    melhortempo=min(melhortempo2)
    while melhortempo not in matriz[k]:
        k=k+1
    return (k+1,melhortempo,list.index(matriz[k],melhortempo))