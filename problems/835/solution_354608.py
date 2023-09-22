def melhor_volta(tempos):
    ''' '''
    dados=()
    corredor=0
    volta=0
    for i in range(len(tempos)):
        if i==0:
            maisRap=min(tempos[i])
        elif maisRap>min(tempos[i]):
            maisRap=min(tempos[i])
            corredor=i+1
            volta=list.index(tempos[i],maisRap)+1
    return (corredor, maisRap,volta)