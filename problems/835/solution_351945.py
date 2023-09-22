def melhor_volta(corrida):
    """retorna quem deu a melhor volta, qual o tempo e em qual volta.(list->tuple)"""
    resultado=[]
    for pessoa in range(len(corrida)):
        for volta in range(len(corrida[pessoa])):
            if min(corrida[pessoa])==corrida[pessoa][volta]:
                resultado.append([pessoa+1,corrida[pessoa][volta],volta+1])
    
    melhoresvoltas=[]
    for i in range(len(resultado)):
    	melhoresvoltas.append(resultado[i][1]
    if resultado[i][1]<=min(melhoresvoltas):
        melhorvolta=resultado[i]
    
    return melhorvolta