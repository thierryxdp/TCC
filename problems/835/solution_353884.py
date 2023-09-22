def melhor_volta(matriz):
    corredor=[]
    tempo=[]
    volta=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            corredor=corredor+[min(matriz[i])]
            tempo=tempo+[min(matriz)]
    return list((list.index(corredor,min(corredor))+1))