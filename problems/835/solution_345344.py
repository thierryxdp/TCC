def melhor_volta(matriz):
    minimo = 0
    for i in range(6):
        if minimo ==0 or min(matriz[i]) <minimo:
            minimo =min(matriz[i])
            volta =list.index(matriz[i], minimo) +1
            corredor =i+1
    return minimo, corredor, volta