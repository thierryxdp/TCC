def melhor_volta(voltas):
	resultado=(0,120,0)
    for i in range(6):
        for j in range(10):
            if voltas[i][j]<resultado[1]:
                resultado= (i+1,voltas[i][j],j+1)
    return resultado