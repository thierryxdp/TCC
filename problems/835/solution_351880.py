def melhor_volta(matriz):
    """Dada uma matriz 6x10 com os tempos em segundo de cada corredor 
    em cada volta, a função retornará uma tupla informando de quem foi
    a menor volta, qual o tempo dessa volta e em que volta.
    matriz -> tuple(int, float, int)"""
    
    melhor_por_volta = []
    
    for i in range(6):
        melhor_por_volta = melhor_por_volta + min(matriz[i])
        
    return (min(melhor_por_volta),list.index(melhor_por_volta, min(melhor_por_volta))+1)