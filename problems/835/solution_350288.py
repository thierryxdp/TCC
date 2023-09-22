def melhor_volta(tempos):
	lista=[]
    for i in range(6):
        for j in range(10):
            lista.append(tempos[i][j])
    for corredor in range(6):
        for volta in range(10):
            if min(lista)==tempos[corredor][volta]:
                return (corredor+1,tempos[corredor][volta],volta+1)