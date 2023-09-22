def melhor_volta(matriz: list) -> tuple:
    
    minimos = []
    linhas = len(matriz)
    colunas = len(matriz[0])
    i = 0
    
    while i < linhas:
        minimos += min(matriz[i])
        i += 1