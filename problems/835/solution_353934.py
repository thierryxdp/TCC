def melhor_volta(matriz):
    corredor=[]
    tempo=[]
    volta=[]
    for i in range(len(matriz)):
    	corredor=corredor+[min(matriz[i])]
        for j in range(len(matriz[i])):
            tempo=tempo+[min(corredor)]
            volta=list.index(tempo, min(tempo))
    return (((list.index(corredor,min(corredor))+1)),min(tempo),(list.index((min(tempo),corredor))))