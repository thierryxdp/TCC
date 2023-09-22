def melhor_volta(corrida):
    tmin=[]
    for corredor in range(len(corrida)):
        tmin.append(min(corrida[corredor]))
    tmin1 = min (tmin)
    for corredor in range (len(corrida)):
        for volta in range(len(corrida[corredor])):
            if (tmin1 == corrida[corredor][volta]):
    return tmin1,corredor+1,volta+1