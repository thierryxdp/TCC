def melhor_volta(matriz):
    menortempo=[]
    for i in range(len(matriz)):
        minimo=min(matriz[i])
        menortempo.append(minimo)
    menor = min(menortempo)
    volta=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == menor:
                volta = j
                corredor = i
    return (corredor+1,menor,volta+1)