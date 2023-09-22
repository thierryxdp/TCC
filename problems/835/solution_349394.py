def melhor_volta(matriz):
    voltas=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            voltas.append(min(matriz[j]))
    return voltas