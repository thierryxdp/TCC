def melhor_volta(matriz: list) -> tuple:
    
    minimos = []
    resultado = []
    linhas = len(matriz)
    colunas = len(matriz[0])
    i = 0
    
    while i < linhas:
        minimos += [min(matriz[i]),]
        i += 1
        
    melhor_jogador = min(minimos)
    menor_tempo = list.index(minimos, min(minimos)
    melhor_volta = list.index(matriz[min(minimos)], min(minimos))
                             
    resultado = [list.index(minimos, min(minimos)) + 1,] + [min(minimos),] 
    
    return resultado