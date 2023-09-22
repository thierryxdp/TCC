def melhor_volta(matriz):
    minimo=[]
    for i in matriz:
        minimos=minimo+[min(i)]
        tempo1=min(minimo)
        x=list.index(minimos,tempo1)
        numeroVolta=list.index(matriz[x],tempo1)
    return (x+1,tempo1,numeroVolta+1)