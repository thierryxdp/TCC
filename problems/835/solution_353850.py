def melhor_volta(tempos):
    for corredor in range(len(tempos)):
        for volta in range(len(tempos[corredor])):
            if nmelhor_tempo < tempos[corredor][volta]:
                nmelhor_tempo = tempos[corredor][volta]
                nmelhor_corredor = corredor
                nmelhor_volta = volta
	return (nmelhor_corredor, nmelhor_tempo, nmelhor_volta)