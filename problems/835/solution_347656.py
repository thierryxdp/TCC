def melhor(corrida):
    tmin1= corrida[0][0]
    for corredor in range(len(corrida)):
        for volta in range(len(corrida[corredor])):
            if tmin1>corrida[corredor][volta]:
    for corredor in range(len(corrida)):
        for volta in range(len(corrida[corredor])):
            if tmin1==corrida[corredor][volta]:
                return tmin1, corredor +1, volta +1