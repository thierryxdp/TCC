def melhor_volta(matriz):
    
    melhor_tempo = matriz [0][0]
    melhor_corredor = 0
    melhor_volta = 0
    for i in range(6):
        
        tempos_corredor = matriz[i]
        
        tempo_corredor = min(tempos_corredor)
        
        if tempo_corredor < melhor_tempo:
            
            melhor_tempo = tempo_corredor