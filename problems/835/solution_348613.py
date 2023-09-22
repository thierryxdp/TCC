def melhor_volta(matriz):
    """Retorna uma tupla informando de quem foi a melhor volta da prova, o seu tempo e em que volta.
    lista --> tupla"""
    
    corredores = []
    
    for i in range(len(matriz)):
        list.append(corredores,min(matriz[i]))
    
    melhor_tempo = min(corredores)
    melhor_corredor = list.index(corredores,melhor_tempo) + 1
    melhor_volta = list.index(matriz,min(matriz[melhor_corredor])) + 1
    
    
    return (melhor_corredor, melhor_tempo, melhor_volta)