def melhor_volta(matriz):
    corredor=[]
    tempo=[]
    volta=[]
    for i in range(len(matriz)):
    	corredor=corredor+[min(matriz[i])]
        for j in range(len(matriz[i])):
            tempo=tempo+[min(corredor)]
            volta=list.index(matriz[list.index(corredor,min(corredor))],min(tempo)+1)
    return (((list.index(corredor,min(corredor))+1)),min(tempo),volta)