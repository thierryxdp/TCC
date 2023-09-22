def melhor_volta(matriz):
    tempos = []
    for i in matriz:
        tempo_posicao = []
        tempo_posicao.append(min(i))
        tempo_posicao.append(i.index(min(i)))
        tempos.append(tempo_posicao)
	return tempo_posicao