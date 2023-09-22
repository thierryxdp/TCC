def melhor_volta(matriz):
    """Função que retorna uma tupla informando de quem foi a melhor volta da prova, com quanto tempo e em qual volta;
    list(list) -> tupla"""
    
    for lista in matriz:
        for tempo in lista:
            melhor_tempo = min(tempo)
    matriz.index(melhor_tempo)
    
    return(matriz.index(melhor_tempo)[0], melhor_tempo, matriz.index(melhor_tempo)[1])