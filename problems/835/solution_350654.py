def melhor_volta (matriz):
    tempos = []
    for tempo_corredor in matriz:
        for tempo in tempo_corredor:
        	list.append(tempos,tempo)
	melhor_tempo = min(tempos)
    melhor_corredor = (list.index(tempos,melhor_tempo)+1)/10
    melhor_volta_corredor = ((list.index(tempos,melhor_tempo)+1)%10)+1
    
    return (melhor_corredor,melhor_tempo,melhor_volta_corredor)