def melhor_volta(mat):
    lista=[]
    for i in mat:
        melhor= min (i)
        lista.append(melhor)
    melhor_volta= min (lista)
    campeao= lista.index(melhor_volta)
    volta= mat[campeao].index(melhor_volta)
    return campeao+1, melhor_volta, volta+1