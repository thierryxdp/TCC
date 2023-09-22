def melhor_volta(matriz):
    melhores_vol=[]
    corredor=0
    ind_volta=[]
    for linha in matriz:
        tempo=min(linha)
        list.append(melhores_vol,tempo)
        list.append(ind_volta,list.index(linha,tempo))
    melhor_tempo=min(melhores_vol)
    corredor=list.index(melhores_vol,melhor_tempo)+1
    melhor_volta=list.pop(ind_volta,corredor)
    return (corredor,melhor_tempo,melhor_volta)