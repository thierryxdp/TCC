def melhor_volta(matriz):
	corredor=0
    melhor_volta=matriz[0].index(min(matriz[0]))

    for i in range(1,len(matriz)):
        x=min(matriz[i])
        if (v<matriz[corredor][melhor_volta]):
            corredor=i
            melhor_volta=matriz[i].index(x)
    return (corredor+1,matriz[corredor][melhor_volta],melhor_volta+1)