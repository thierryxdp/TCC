def melhor_volta(m):
    melhor_corredor = 0
    melhor_tempo = 0
    melhor_volta = 0
    for i in range(0,6):
        for j in range(0,10):
            melhor_tempo = min(m[i][j])
    return (melhor_tempo,)