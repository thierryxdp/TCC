def melhor_volta(m):
    '''retorna de quem foi a melhor volta, o tempo dessa volta e em qual volta foi
    list -> tuple'''
    nlin=len(m)
    ncol=len(m[0])
    melhores_voltas=[]
    qual_volta=[]
    for i in range(nlin):
        list.append(melhores_voltas,min(m[i]))
        list.append(qual_volta,list.index(m[i],min(m[i]))+1)
    melhor_volta=min(melhores_voltas)
    return (list.index(melhores_voltas,melhor_volta)+1,melhor_volta,qual_volta[list.index(melhores_voltas,melhor_volta)])