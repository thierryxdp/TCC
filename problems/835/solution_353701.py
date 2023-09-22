def melhor_volta(m):
    melhor_tempo = m[0][0]
    melhor_corredor = 0
    melhor_volta = 0
    for i in range(6):
        tempos_corredor = m[i]
        tempo_corredor = min(tempos_corredor)
        if tempo_corredor < melhor_tempo:
            melhor_tempo = tempo_corredor
            melhor_corredor = i+1
            melhor_volta = list.index(m[i],melhor_tempo)
    return (melhor_corredor, melhor_tempo, melhor_volta)