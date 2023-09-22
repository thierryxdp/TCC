def melhor_volta(m):
    melhores_tempos=[]
    for i in range(len(m)):
        menor_tempo=min(m[i])
        list.append(melhores_tempos,menor_tempo)
    min_tempo.min(melhores_tempos)
    melhor_piloto=melhores_tempos.index(min_tempo)
    volta=m[melhor_piloto].index(min_tempo)
    return melhor_piloto+1,min_tempo,volta+1