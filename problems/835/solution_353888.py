def melhor_volta(matriz):
    corredor=[]
    tempo=[]
    volta=[]
    for i in range(len(matriz)):
            corredor=corredor+[min(matriz[i])]
            tempo=tempo+[min(matriz)]
    return ((list.index(corredor,min(corredor))+1))