def melhor_volta (matriz)
    tempos=[]
    for i in range(6):
        list.append(tempos,min(matriz[i]))
    mais_rapido=min(tempos)
    corredor=tempos.index(mais_rapido)+1
    qual_volta=matriz[corredor-1].index(mais_rapido)+1
    
    return (corredor,mais_rapido,qual_volta)