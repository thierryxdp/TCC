def melhor_volta(matriz):
    voltasrap=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            voltasrap=voltasrap+min(matriz[i])
        return voltas rap