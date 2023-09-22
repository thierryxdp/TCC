def melhor_volta(corrida):
    melhores=()
    for volta in corrida:
        melhores.append(min(corrida(volta)))
    
    
    return melhores