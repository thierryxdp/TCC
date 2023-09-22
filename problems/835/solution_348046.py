def melhor_volta(tempos):
    '''dado uma matriz com os tempos de cada corredor
    retirn qual corredor fez o menor tempo,assim como o tempo
    e em qual volta
    list->tup'''
    #menor tempo de cada participante
    menortempo=[]
    for i in range(len(tempos)):
        menortempo+=[min(tempos[i])]
    corredor=menortempo.index(min(menortempo))
    volta=tempos[corredor].index(min(tempos[corredor]))
    return (corredor+1,min(menortempo),volta+1)