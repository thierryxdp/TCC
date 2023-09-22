def melhor_volta(matriz):
    corredor=[]
    tempo=[]
    volta=[]
    for i in range(len(matriz)):
    	corredor=corredor+[min(matriz[i])]
        for j in range(len(matriz[i])):
            tempo=tempo+[min(corredor)]
    corredor1=(list.index(corredor,min(corredor))+1)
#(list.index((min(matriz[corredor1])),)
    return (corredor1,min(tempo),(list.index((min(matriz[corredor1])))