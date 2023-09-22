def melhor_volta(matriz):
    """
    Código que define a melhor volta de uma matriz contendo o 
    tempo de corrida dos corredores
    :matriz --> lista:
    :return --> tupla :
    """
    
    melhor_tempo = matriz[0][0]
    
    for i in range(len(matriz)):
        tempo_corredor = min(matriz[i])
        
        if tempo_corredor < melhor_tempo:
            melhor_tempo = tempo_corredor
            melhor_corredor = i
            
    volta = list.index(matriz[melhor_corredor], melhor_tempo)
    
    return melhor_corredor + 1, melhor_tempo, volta + 1