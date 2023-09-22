def melhor_volta(corrida):
    """retorna quem deu a melhor volta, qual o tempo e em qual volta.(list->tuple)"""
    resultado=[]
    for pessoa in range(len(corrida)):
        for volta in range(len(corrida[pessoa])):
            if min(corrida[pessoa])==corrida[pessoa][volta]:
                resultado[pessoa+1]=pessoa+1,corrida[pessoa][volta],volta+1
    
    
    return resultado