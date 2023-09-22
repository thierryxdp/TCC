def melhor_volta(corrida):
    
    mT = corrida[0][0]
    
    for pessoa, voltas in enumerate(corrida):
        for volta, tempo in enumerate(voltas):
            if mT >= tempo:
                mT = tempo
                mV = volta + 1
                mP = pessoa + 1
    return mP, mT, mV