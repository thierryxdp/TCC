def melhor_volta(matriz):
    i=0
    mtc=[]
    mvc=[]
    while i<6:
        mt=min(matriz[i])
        mtc+=[mt]
        mv=matriz[i].index(mt)
        mvc+=[mv,]
        i +=1
    tempo= min(mtc)
    piloto= mtc.index(tempo)
    volta=mvc[piloto]
    return (piloto+1, tempo  volta+1)