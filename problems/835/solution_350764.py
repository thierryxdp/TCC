def melhor_volta(m):
    melhores_tempos = [0]
    voltas = [0]
    for i in range(len(m)):
        list.append(min(m[i]), melhores_tempos)
        list.append(list.index(min(m[i])),voltas)
    melhor_corredor = list.index(min(melhores_tempos))
    melhor_volta = voltas[melhor_corredor]
    return (melhor_corredor,melhor_volta)