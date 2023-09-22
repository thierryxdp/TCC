def melhor_volta(tempos):
	for i in range(5):
        for j in range(9):
            lista.append(tempos[i][j])
    for corredor in range(5):
        for volta in range(9):
            if min(lista)==tempos[corredor][volta]:
                return (corredor+1,tempos[corredor][volta],volta+1)