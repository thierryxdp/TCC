def melhor_volta (matriz):
    tempos = []
    for tempo_corredor in matriz:
        for tempo in tempo_corredor:
        tempos.append(tempo)
	melhor_tempo = min(tempos)
    melhor_corredor = int((tempo.index(melhor_tempo)+1)/10)
    melhor_volta_corredor = ((tempo.index(melhor_tempo)+1)%10)+1
    
    return (melhor_corredor,melhor_tempo,melhor_volta_corredor)