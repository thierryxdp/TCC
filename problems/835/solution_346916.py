def melhor_volta(matriz):
    # pilotos = 6 = linhas
    # voltas = 10 = colunas
    tempos_minimos = []
    for p in range(len(matriz)):
        #print(f'corredor: {p+1}')
        minim = min(matriz[p])
        tempos_minimos.append(minim)
        #print(f'tempo min: {minim}s')
    melhor_corredor = tempos_minimos.index(min(tempos_minimos))
    melhor_tempo = (min(tempos_minimos))
    volta_mlr_tempo = matriz[melhor_corredor].index(melhor_tempo)+1
    return (melhor_corredor+1,melhor_tempo,volta_mlr_tempo )