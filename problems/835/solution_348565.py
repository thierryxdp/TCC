def melhor_volta(matriz):
    
    tempo = min(min(matriz))
    corredor = matriz.index(min(matriz))
    num_volta = matriz[corredor].index(tempo)
    
    return (corredor + 1, tempo, num_volta + 1)