def melhor_volta(matriz):
    """Retorna uma tupla informando de quem foi a melhor volta da prova, o seu tempo e em que volta.
    lista --> tupla"""
    
    corredores = []
    
    for i in range(len(matriz)):
        list.append(corredores,min(matriz[i]))
    
    melhor_tempo = min(corredores)
    melhor_corredor = list.index(corredores,melhor_tempo)
    melhor_volta = list.index(matriz[melhor_corredor],melhor_tempo)
    
    
    return (melhor_corredor + 1, melhor_tempo, melhor_volta + 1)