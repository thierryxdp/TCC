def melhor_volta(matriz):
    
    melhor_tempo = matriz[0][0]
    melhor_corredor = 0
    melhor_volta = 0
    
    for i in range(6):
        # busca o tempo de cada corredor I
        tempos_corredor = matriz[i]
        
        # encontra o melhor tempo
        # pro corredor
        tempo_corredor = min(tempos_corredor)
        
        if tempo_corredor < melhor_tempo:
            # encontramos um melhor tempo
            melhor_tempo = tempo_corredor
            
            # salva quem é melhor corredor
            melhor_corredor = i
	
    melhor_volta = list.index(matriz[melhor_corredor], melhor_tempo)
    
    return melhor_corredor, melhor_tempo, melhor_volta