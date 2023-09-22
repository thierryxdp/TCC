def melhor_volta(corrida):
    
    mT = corrida[0][0]
    
    for voltas, pessoa in enumerate(corrida):
        for tempo, volta in enumerate(voltas):
            if mT <= tempo:
                mT = tempo
                mV = volta + 1
                mP = pessoa + 1
    return mP, mT, mV