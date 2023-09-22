def melhor_volta (matriz):
    tempos = []
    for tempo_corredor in matriz:
        for tempo in tempo_corredor:
        	list.append(tempos,tempo)
	melhor_tempo = min(tempos)
    melhor_corredor1 = (list.index(tempos,melhor_tempo)+1)/10
    melhor_volta_corredor = ((list.index(tempos,melhor_tempo)+1)%10)+1
    melhor_corredor2= round(melhor_corredor1,0)
    melhor_corredor= int(melhor_corredor2)
    return (melhor_corredor,melhor_tempo,melhor_volta_corredor)