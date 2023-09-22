def melhor_volta(matriz):
    corredor=[]
    tempo=[]
    volta=[]
    for i in range(len(matriz)):
    	corredor=corredor+[min(matriz[i])]
        for j in range(len(matriz[i])):
            tempo=tempo+[min(matriz[i])]
    return (((list.index(corredor,min(corredor))+1)),((list.index(tempo,min(tempo)))