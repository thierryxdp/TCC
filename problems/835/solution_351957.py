def melhor_volta(corrida):
    
    mT = corrida[0][0]
    
    for pessoa, voltas  in enumerate(corrida,1):
        for volta, tempo in enumerate(voltas,1):
            if mT >= tempo:
                mT = tempo
                mV = volta
                mP = pessoa
                
    return mP, mT, mV