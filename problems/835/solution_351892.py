def melhor_volta(matriz):
    """Dada uma matriz 6x10 com os tempos em segundo de cada corredor 
    em cada volta, a função retornará uma tupla informando de quem foi
    a menor volta, qual o tempo dessa volta e em que volta.
    matriz -> tuple(int, float, int)"""
    
    melhor_por_volta = []
    
    for i in range(6):
        melhor_por_volta = melhor_por_volta + [min(matriz[i])]
    
    
    melhor_volta = (list.index(melhor_por_volta, min(melhor_por_volta))+1)
    melhor_tempo = min(melhor_por_volta)
    
    melhor_piloto = 0
    
    for i in range(6):
        if melhor_tempo in matriz[i]:
            melhor_piloto = list.index(matriz[i], melhor_tempo)+1
            
            
    return (melhor_volta,melhor_tempo,melhor_piloto)