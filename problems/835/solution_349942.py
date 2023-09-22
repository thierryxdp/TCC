def melhor_volta(matriz):
    m=[]
    for i in matriz:
        m=m+[min(i)]
        tempoMin=min(m)
        x=list.index(m,tempoMin)
        melhorVolta=list.index(matriz[x],tempoMin)
        return (x+1,tempoMin,melhorVolta+1)