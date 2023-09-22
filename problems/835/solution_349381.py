def melhor_volta(matriz: list)-> tuple:
    """
    
    """
    melhor_prova=()
    
    for corredor in range(len(matriz)):
        melhor_volta=()
        
        for volta in range(len(matriz[corredor])):
            melhor_volta += ((corredor+1 , matriz[corredor][volta] , volta+1),)
        melhor_prova += melhor_volta
    tempo = ()

    
    for termo in range(len(melhor_prova)):
        tempo += (melhor_prova[termo][1],)
    
    minimo = min(tempo)

    
    for  termo in range(len(melhor_prova)):
        indice = 0
        if minimo == melhor_prova[termo][2]:
            indice = termo
            
    
    return melhor_prova[indice]