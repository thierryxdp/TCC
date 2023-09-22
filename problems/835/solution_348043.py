def melhor_volta(tempos):
    #menor tempo de cada participante
    menortempo=[]
    for i in range(len(tempos)):
        menortempo+=[min(tempos[i])]
    corredor=menortempo.index(min(menortempo))
    volta=tempos[corredor].index(min(tempos[corredor]))
    return (corredor+1,menortempo,volta)