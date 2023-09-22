def melhor_volta(matriz):
    posi=0
    melhor_tempo_corredor=[]
    melhor_volta_corredor=[]
    while posi<6:
        melhor_tempo = min(matriz[posi])
        melhor_tempo_corredor+=[melhor_tempo,]
        melhor_lap = matriz[posi].index(melhor_tempo)
        melhor_volta_corredor+=[melhor_lap,]
        posi+=1
    t=min(melhor_tempo_corredor)
    piloto=melhor_tempo_corredor.index(t)
    volta=melhor_volta_corredor[piloto]
    return (piloto+1,t,volta+1)