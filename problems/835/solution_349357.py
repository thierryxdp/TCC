def melhor_volta(voltas):
	resultado=[0,]
    corredor=0
    for i in range(6):
        for j in range(10):
            if voltas[i][j]<corredor:
                resultado=