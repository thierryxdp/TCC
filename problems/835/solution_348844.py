def melhor_volta(matriz: list) -> tuple:
    
    minimos = []
    resultado = []
    linhas = len(matriz)
    colunas = len(matriz[0])
    i = 0
    
    while i < linhas:
        minimos += [min(matriz[i]),]
        i += 1
        
    melhor_jogador = list.index(minimos, min(minimos)) + 1
    melhor_tempo = min(minimos)
    melhor_partida = list.index(matriz[list.index(minimos, min(minimos))], min(minimos)) + 1
    
    list.append(melhor_jogador, resultado)
    list.append(melhor_tempo, resultado)
    list.append(melhor_partida, resultado)
    
    return resultado