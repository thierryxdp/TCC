def melhor_volta(matriz):
    tempo=[] 
    for i in matriz:
        tempo=tempo+[min(i)]
    ment=min(tempo)
    corredor=list.index(tempo,ment)
    volta=list.index(matriz[corredor],ment)
    return (corredor+1,ment,volta+1)