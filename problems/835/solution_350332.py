def melhor_volta(matriz):
    menores=[]
    for i in range(len(matriz)):
        menores.append(min(matriz[i]))
    menor=min(menores)
    corredor=menores.index(menor)
    volta=matriz[corredor].index(menor)
    resultado = (menor,corredor+1,volta+1)
    return resultado