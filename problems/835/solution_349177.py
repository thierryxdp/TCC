def melhor_volta(l):
    melhores_voltas = []
    for i in range(len(l)):
        melhor_volta = min(l[i])
        melhores_voltas.append(melhor_volta)
    melhor_volta_geral = min(melhores_voltas)
    piloto = melhores_voltas.index(melhor_volta_geral) + 1
    nr_volta = l[piloto - 1].index(melhor_volta_geral) + 1
    return piloto, melhor_volta_geral, nr_volta