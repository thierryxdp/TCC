def melhor_volta(m):
    melhores_tempos = [0]
    melhores_voltas = [0]
    for i in range(len(m)):
        list.append(melhores_tempos, min(m[i]))
        list.append(melhores_voltas, list.index(m[i],min(m[i])+1))
    melhor_tempo = min(melhores_tempos[1:])
    melhor_corredor = list.index(melhores_tempos,melhor_tempo)
    melhor_volta = melhores_voltas[melhor_corredor]
    return (melhor_corredor, melhor_tempo, melhor_volta)