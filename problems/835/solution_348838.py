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
    melhor_partida = list.index(matriz[list.index(minimos, min(minimos))], min(minimos))
    
    return [melhor_jogador,] + [melhor_tempo,] + [melhor_partida,]