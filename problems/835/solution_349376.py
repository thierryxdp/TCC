def melhor_volta(matriz: list)-> tuple:
    """
    
    """
    melhor_prova=()
    
    for corredores in range(1,7):
        melhor_volta=()
        
        for voltas in range(1,11):
            melhor_volta += (corredor, matriz[corredores][voltas] ,volta)
    	melhor_prova += melhor_volta
    tempo = ()

    for i in range(len(melhor_prova)):
        tempo += (melhor_prova[i][1],)
    
    minimo = min(tempo)

    for i in range(len(melhor_prova)):
        indice = 0
        if minimo == melhor_prova[i][1]:
            indice = i
            
    return melhor_prova[indice]