def melhor_volta(matriz: list)-> tuple:
    """
    
    """
    melhor_prova=()
    
    for corredor in range(1,7):
        melhor_volta=()
        
        for volta in range(1,11):
            melhor_volta = melhor_volta + (corredor, matriz[corredor][volta],volta)
    tempo = ()
    for i in range(len(melhor_volta)):
        tempo += (melhor_prova[i][1],)
    
    minimo = min(tempo)
    for i in range(len(melhor_voltar)):
        indice = 0
        if minimo == melhor_prova[i][1]:
            indice = i
            
    return melhor_prova[indice]