def melhor_volta(tempos):
    menores=[]
    for i in tempos:
    	menores.append(min(i))
    corredor=menores.index(min(menores))+1
    tempo=min(menores)
    volta=tempos[corredor-1].index(min(menores))+1
    return (corredor,tempo,volta)