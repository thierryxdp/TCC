def melhor_volta(matriz):
    lista=[]
    for i in matriz:
        melhor= min (i)
        lista.append(i)
    melhor_volta= min (lista)
    campeao= lista.index(melhor_volta)
    volta= matriz[campeao-1].index(melhor_volta)
    return campeao+1, melhor_volta, volta+1