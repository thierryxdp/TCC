def melhor_volta(m):
    melhores_tempos = [0]
    voltas = [0]
    for i in range(len(m)):
        list.append(melhores_tempos,min(m[i]))
        list.append(voltas,list.index(m[i],min(m[i]))
    melhor_tempo = min(melhores_tempos)
    melhor_corredor = list.index(melhores_tempos,melhor_tempo)
    melhor_volta = voltas[melhor_corredor]
    return (melhor_corredor,melhor_tempo,melhor_volta)