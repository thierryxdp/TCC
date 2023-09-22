def melhor_volta(tempos):
    #menor tempo de cada participante
    menortempo=[]
    for i in range(len(tempos)):
        menortempo+=[min(tempos[i])]
    return menortempo